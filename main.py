from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import pymupdf
import joblib

app = FastAPI()


# Load trained ML model and TF-IDF vectorizer
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")


@app.get("/")
def home():
    return {"message": "Fake Job Scam Detection API is running"}


# Request format for job prediction
class JobData(BaseModel):
    text: str


@app.post("/predict")
def predict_job(job: JobData):

    # Convert job text into TF-IDF features
    text_tfidf = vectorizer.transform([job.text])

    # Predict
    prediction = model.predict(text_tfidf)[0]

    if prediction == 1:
        result = "Fake"
    else:
        result = "Real"

    return {
        "prediction": result
    }


@app.post("/extract-pdf")
async def extract_pdf(file: UploadFile = File(...)):

    pdf_bytes = await file.read()

    document = pymupdf.open(
        stream=pdf_bytes,
        filetype="pdf"
    )

    text = ""

    for page in document:
        text += page.get_text()

    document.close()

    return {
        "filename": file.filename,
        "extracted_text": text
    }