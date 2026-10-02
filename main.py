from fastapi import FastAPI, UploadFile, File
import pymupdf

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Fake Job Scam Detection API is running"}


@app.post("/extract-pdf")
async def extract_pdf(file: UploadFile = File(...)):
    pdf_bytes = await file.read()

    document = pymupdf.open(stream=pdf_bytes, filetype="pdf")

    text = ""

    for page in document:
        text += page.get_text()

    document.close()

    return {
        "filename": file.filename,
        "extracted_text": text
    }