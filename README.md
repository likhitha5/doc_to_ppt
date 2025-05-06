# 📄 Doc-to-Presentation Converter (Doc2PPT)

A GenAI-powered tool that takes a PDF document, extracts key content and images, and generates a structured presentation. Built with a React frontend and a FastAPI backend. Supports Google Gemini (and placeholders for OpenAI and Hugging Face).

---

## 🚀 Features

- Upload a PDF document.
- Extract text, images, and structured headings.
- Generate presentation slides using Google Gemini (`gemini-pro`).
- Built-in support for switching between AI models (Gemini, OpenAI, HuggingFace).
- Preview slides in a clean UI (React).
- Currently hosted **locally**.

Notes: 
Only PDF files are supported currently.
Model dropdown includes OpenAI and Hugging Face options, but they are not yet implemented.
Content is not stored, everything runs locally on your machine.
Results are based on the Gemini model's understanding of the document structure.

---

## 🏗️ Project Structure

project_1/
├── frontend/ # React app
├── backend/ # FastAPI backend
└── README.md

---

## 🧩 Setup Instructions

Clone the repository

```bash
git clone https://github.com/likhitha5/doc_to_ppt.git
cd doc_to_ppt
```

## Backend Setup (FastAPI)

cd backend
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows

pip3 install -r requirements.txt

Create a .env file in the backend directory:
ini
Copy
Edit
GEMINI_API_KEY=your_gemini_api_key_here
🔐 Replace your_gemini_api_key_here with your actual Google API Key for Gemini.

Run the backend server:
uvicorn main:app --reload
This will start the FastAPI server at: http://127.0.0.1:8000


## Frontend Setup (React)
cd ../frontend
npm install
npm start
This will start the React development server at: http://localhost:3000

## Environment Variables
Only one required for now:
GEMINI_API_KEY – Google Gemini API key
To get this key, visit: https://aistudio.google.com/app/apikey

## Sample Workflow
Select a model (currently only Gemini works).
Upload a .pdf file with structured content.
Click Submit.
See slide-based output generated on the frontend.

## Tech Stack
Frontend: React, Material UI

Backend: FastAPI, PyMuPDF (fitz), Requests

## AI Models: 
Google Gemini (generativelanguage.googleapis.com)

## Future Plans
Add support for OpenAI and Hugging Face
Export presentation as .pptx
Deploy backend and frontend on cloud (e.g., AWS, Vercel)