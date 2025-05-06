import os
import requests
import openai
from typing import Dict, List
from dotenv import load_dotenv
from prompts import PRESENTATION_TEMPLATE
import json
import re
import base64
import random
from collections import defaultdict
import content_extractor

# Load environment variables from a .env file (API keys, etc.)
load_dotenv()

# Get the Gemini API key from environment variables
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def generate_presentation(text: str, images: list, audience_type: str, instructions: str, model_provider: str, headings: list) -> Dict:
    """
    Generates a presentation using the specified model provider (Gemini, HuggingFace, OpenAI).

    Arguments:
    - text (str): Main content for the presentation.
    - images (list): List of image file paths.
    - audience_type (str): Type of audience (e.g., educational, executive).
    - instructions (str): Custom instructions for the presentation.
    - model_provider (str): Model provider ('gemini', 'huggingface', 'openai').
    - headings (list): List of headings for content organization.

    Returns:
    - Dict: Generated slides in JSON format.
    """
    # Call the appropriate model provider function based on the input
    print(model_provider)
    if model_provider == "gemini":
        return use_gemini(text, images, audience_type, instructions, headings)
    elif model_provider == "huggingface":
        return use_huggingface(text, images, audience_type, instructions, headings)
    elif model_provider == "openai":
        return use_openai(text, images, audience_type, instructions, headings)
    else:
        # Return an error slide if an invalid model provider is provided
        return {"slides": [{"type": "content", "title": "Error", "content": ["Unknown model provider."]}]}


def use_gemini(text: str, images: list, audience_type: str, instructions: str, headings: list):
    # Prepare the URL for the Gemini API with the API key as a query parameter
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"
    
    # Create the heading-to-image mapping string
    heading_image_mapping_str = content_extractor.get_heading_image_mapping(headings, images)
    
    # Format the presentation prompt with the provided parameters
    prompt = PRESENTATION_TEMPLATE.format(
        audience_type=audience_type,
        instructions=instructions,
        text=text,
        heading_image_mapping=heading_image_mapping_str
    )

    # Prepare the request data for the Gemini API
    data = {
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    }

    # Send the POST request to the Gemini API
    response = requests.post(url, json=data)

    # Check for a successful response
    if response.status_code == 200:
        # Parse the response JSON to extract the generated slides content
        result = response.json()
        slides_content = result.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "")
        slides = content_extractor.extract_slides_from_content(slides_content)  # Function to parse the content into slides
        return slides
    else:
        # Handle the error if the request fails
        print(f"Error: Failed to generate content, Status Code: {response.status_code}")
        return [{"type": "content", "title": "Error", "content": ["Failed to generate presentation."]}]

def use_openai(text: str, images: list, audience_type: str, instructions: str, headings: list):
    # Placeholder for OpenAI functionality (to be implemented later)
    return {"slides": [{"type": "content", "title": "Error", "content": ["Model yet to be implemented."]}]}

def use_huggingface(text: str, images: list, audience_type: str, instructions: str, headings: list) -> Dict:
    # Placeholder for HuggingFace functionality (to be implemented later)
    return {"slides": [{"type": "content", "title": "Error", "content": ["Model yet to be implemented."]}]}
