# 📄 Doc-to-Presentation Converter (Doc2PPT)

A GenAI-powered tool that takes a PDF document, extracts key content and images, and generates a structured presentation. Built with a React frontend and a FastAPI backend. Supports Google Gemini (and placeholders for OpenAI and Hugging Face).

---

## 🚀 Features

- Upload a PDF document.
- Extract text, images, and structured headings.
- Generate presentation slides using Google Gemini (`gemini-pro`).
- Built-in support for switching between AI models (Gemini, OpenAI, HuggingFace).
- Preview slides in a clean UI (React).
- Currently hosted at http://65.0.34.91:3000. Can be run/tested locally too (Refer below).

Notes: 
Only PDF files are supported currently.
Model dropdown includes OpenAI and Hugging Face options, but they are not yet implemented.
Content is not stored, everything runs locally on host/your machine.
Results are based on the Gemini model's understanding of the document structure.

---

## 🏗️ Project Structure

root/
 - frontend/ # React app
 - backend/ # FastAPI backend
 - README.md

---
## How to test application - on Deployed Server

Application link : http://65.0.34.91:3000
Input fields:
 - Choose AI Model (Currently only gemini supported)
 - Choose Audience Type
 - Add if any extra instructions needed
 - Upload document (currently only pdf supported)
 - Click generate.

## 🧩 Setup Instructions Locally

Clone the repository

```bash
git clone https://github.com/likhitha5/doc_to_ppt.git
cd doc_to_ppt
```

## Backend Setup (FastAPI)

```bash
cd backend
python -m venv venv
source venv/bin/activate 

pip install -r requirements.txt
```

## Environment Variables
Only one required for now:
Create a .env file in the backend directory:
```bash
echo "GEMINI_API_KEY=<your-gemini-api-key>" > .env
```
GEMINI_API_KEY – Google Gemini API key
To get this key, visit: https://aistudio.google.com/app/apikey
Replace your_gemini_api_key_here with your actual Google API Key for Gemini.

## Run Backend Server
```bash
uvicorn main:app --reload
```
This will start the FastAPI server at: http://localhost:8000

## Frontend Setup (React)
```bash
cd ../frontend
npm install
npm start
```
This will start the React development server at: http://localhost:3000

## Sample Workflow
- Select a model (currently only Gemini works).
- Select Audience Type
- Upload a .pdf file (currently only pdf is supoorted)
- Click Submit.
- See slide-based output generated on the frontend.

## Tech Stack
- Frontend: React, Material UI
- Backend: FastAPI, PyMuPDF (fitz), Requests

## AI Models: 
Google Gemini (generativelanguage.googleapis.com)

## Future Plans
- Add support for OpenAI and Hugging Face
- Export presentation as .pptx
- Support multiple support document types (docx etc..)