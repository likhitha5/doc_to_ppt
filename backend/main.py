from fastapi import FastAPI, File, UploadFile, Form
from io import BytesIO
from fastapi.middleware.cors import CORSMiddleware
from typing import Tuple, List
import uuid
from zipfile import ZipFile
from content_extractor import extract_content_from_pdf
from fastapi.staticfiles import StaticFiles
import mimetypes
from ppt_generator import generate_presentation 

app = FastAPI()

# Allow all origins (you can specify a list of allowed origins as well)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify a list like ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

"""
    This FastAPI route handles file uploads. It accepts a PDF file, extracts content (text, images, and headings) 
    using the `extract_content_from_pdf` function, and then generates a presentation based on the extracted content. 
    The presentation is generated using a specified model (e.g., "gemini") and customized according to audience type 
    and additional instructions. It then returns the generated presentation slides.
"""
@app.post("/upload")
async def upload(file: UploadFile = File(...), model: str = Form("gemini"), audience_type: str = "general", instructions: str = "Generate an engaging presentation."):
    file_bytes = await file.read()
    file_type, _ = mimetypes.guess_type(file.filename)

    if file_type == 'application/pdf':
        text, images, headings = extract_content_from_pdf(file_bytes)
    else:
        return {"error": "Unsupported file type."}

    # Generate the presentation slides based on the extracted text
    print(model)
    slides = generate_presentation(text, images, audience_type, instructions, model, headings)
    return {"slides": slides}

app.mount("/uploads", StaticFiles(directory="../saved_uploads"), name="uploads")


app = FastAPI()

# Allow all origins (you can specify a list of allowed origins as well)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify a list like ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

"""
    This FastAPI route handles file uploads. It accepts a PDF file, extracts content (text, images, and headings) 
    using the `extract_content_from_pdf` function, and then generates a presentation based on the extracted content. 
    The presentation is generated using a specified model (e.g., "gemini") and customized according to audience type 
    and additional instructions. It then returns the generated presentation slides.
"""
@app.post("/upload")
async def upload(file: UploadFile = File(...), model: str = Form("gemini"), audience_type: str = "general", instructions: str = "Generate an engaging presentation."):
    file_bytes = await file.read()
    file_type, _ = mimetypes.guess_type(file.filename)

    if file_type == 'application/pdf':
        text, images, headings = extract_content_from_pdf(file_bytes)
    else:
        return {"error": "Unsupported file type."}

    # Generate the presentation slides based on the extracted text
    print(model)
    slides = generate_presentation(text, images, audience_type, instructions, model, headings)
    return {"slides": slides}

app.mount("/uploads", StaticFiles(directory="../saved_uploads"), name="uploads")
