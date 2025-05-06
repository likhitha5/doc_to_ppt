import fitz  # PyMuPDF
import os
import base64
from typing import Tuple, List, Dict
from collections import defaultdict
import json
import re
import random

def extract_content_from_pdf(file_bytes: bytes, save_dir: str = "../saved_uploads") :
    """
    Extract text, embedded images and headings from a PDF file and save them locally.

    Args:
        file_bytes (bytes): PDF file content.
        save_dir (str): Directory to save text and images.

    Returns:
        Tuple containing:
            - Combined plain text.
            - List of image metadata: {"format": "png", "data": "<base64 string>", "file_path": <image_filename>}
    """
    os.makedirs(save_dir, exist_ok=True)

    pdf_document = fitz.open(stream=file_bytes, filetype="pdf")
    text = ""
    images = []
    headings = extract_headings_from_pdf(pdf_document)  # This returns the headings for each page

    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        text += page.get_text()
        # Extract images from page
        image_list = page.get_images(full=True)

        # Get heading for the page
        heading = headings[page_num] if page_num < len(headings) else "No_Heading"

        # Normalize heading to be file-system safe (e.g., lowercasing, replacing spaces with underscores)
        heading_normalized = heading.lower().replace(" ", "_")

        if image_list:
            for img_index, img in enumerate(image_list):
                xref = img[0]
                base_image = pdf_document.extract_image(xref)
                image_bytes = base_image["image"]
                image_format = base_image["ext"]
                image_b64 = base64.b64encode(image_bytes).decode("utf-8")

                # Save image file with heading as part of the name
                image_filename = f"{heading_normalized}_{img_index+1}.{image_format}"
                image_path = os.path.join(save_dir, image_filename)
                with open(image_path, "wb") as f:
                    f.write(image_bytes)

                print(image_path)

                images.append({
                    "format": image_format,
                    "data": image_b64,
                    "file_path": image_filename
                })

    # Save text to file
    text_path = os.path.join(save_dir, "extracted_text.txt")
    with open(text_path, "w", encoding="utf-8") as f:
        f.write(text)
    
    return text, images, headings

def extract_headings_from_pdf(pdf_document):
    """
    This function extracts headings from a PDF document by identifying the largest bold text 
    on each page, which is likely to be the main heading. It iterates through all pages of 
    the document, checks for bold text with a font size of at least 10, and collects the 
    largest bold text on each page as the heading.
    """
    page_headings = []
    
    # Iterate over all pages in the document
    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        
        # Get detailed layout information (use "dict" for extracting font and layout details)
        blocks = page.get_text("dict")['blocks']
        
        # List to store all bold text candidates on the page
        bold_texts = []
        
        # Process each block
        for block in blocks:
            if block['type'] == 0:  # Text block
                for line in block['lines']:
                    for span in line['spans']:
                        text = span['text'].strip()
                        font_size = span['size']
                        font = span['font']
                        
                        # Only consider bold text
                        if 'bold' in font.lower() and font_size >= 20:
                            bold_texts.append((text, font_size))
        
        # Sort bold texts by font size in descending order and pick the top one
        bold_texts.sort(key=lambda x: x[1], reverse=True)
        
        # Add the top bold text (largest font) as the heading for the page
        if bold_texts:
            page_headings.append(bold_texts[0][0])  # Only the text of the largest bold font
    
    return page_headings

def get_heading_image_mapping(headings: List[str], images: List[Dict]) -> str:
    """
    Associates saved image file paths with relevant headings based on file name matching.

    Args:
        headings (List[str]): List of selected headings (1 per page).
        images (List[Dict]): Each dict contains image metadata including 'file_path'.

    Returns:
        str: A JSON-like string mapping of headings to image paths (to include in prompt).
    """
    mapping = defaultdict(list)

    for heading in headings:
        clean_heading = heading.lower().replace(" ", "_")
        for img in images:
            img_path = os.path.basename(img['file_path']).lower()
            if clean_heading in img_path:
                mapping[heading].append(img['file_path'])

    # Convert to JSON-style string for prompt formatting
    mapping_str = "{\n"
    for heading, paths in mapping.items():
        if paths:
            chosen_paths = ', '.join(f'"{path}"' for path in paths)
            mapping_str += f'    "{heading}": [{chosen_paths}],\n'
    mapping_str += "}"

    return mapping_str

def extract_slides_from_content(slides_content):
    # Remove triple backtick wrapper like ```json ... ```
    """
        Slides format :
        "slides": [
        {{
            "type": "title|content|summary",
            "title": "Slide title",
            "content": ["bullet point 1", "bullet point 2"],
            "notes": "speaker notes",
            "image": "saved_uploads/filename.png" or null
        }}
    ]
    """
    match = re.search(r'```(?:json)?\s*(\{[\s\S]*?\})\s*```', slides_content)
    
    if match:
        json_str = match.group(1)
    else:
        # Fallback: assume the whole string is raw JSON
        json_str = slides_content.strip()
    
    try:
        data = json.loads(json_str)
        return data.get("slides", [])
    except json.JSONDecodeError as e:
        print("❌ JSON decode error:", e)
        return []
