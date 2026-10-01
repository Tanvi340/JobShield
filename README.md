# 🛡️ JobShield — Fake Job & Internship Scam Detection

> **Verify before you apply.**

JobShield is an AI-assisted web application designed to analyze job and internship opportunities and identify potential scam indicators before a user applies or shares sensitive information.

The system accepts multiple types of inputs such as job descriptions, URLs, recruiter details, screenshots, and PDF advertisements. It combines **OCR, NLP, machine learning, rule-based detection, company verification, recruiter verification, and URL analysis** to generate an explainable risk assessment.

---

## 🚀 Features

* 📄 Analyze pasted job descriptions
* 🔗 Analyze job URLs
* 📧 Analyze recruiter email addresses
* 📱 Analyze recruiter phone numbers
* 🖼️ Upload WhatsApp/Telegram/LinkedIn screenshots
* 📑 Upload job advertisement PDFs/images
* 🔍 OCR-based text extraction
* 🧠 NLP and ML-based scam detection
* ⚠️ Scam keyword and pattern detection
* 🏢 Company verification
* 👤 Recruiter verification
* 🌐 URL and domain analysis
* 🏷️ Scam-type classification
* 📊 Multi-signal risk scoring
* 💡 Explainable risk factors and evidence
* 💾 Analysis history and user feedback
* 📈 Admin dashboard for system statistics

---

# 🧩 Problem Statement

Fake job and internship scams are increasingly presented through professional-looking advertisements, social media messages, emails, and recruitment platforms.

Users may encounter:

* Fake recruiters
* Fake companies
* Upfront registration fees
* Security deposits
* Fake internships
* Unrealistic salary promises
* Task-based scams
* Requests for sensitive information
* Suspicious application websites
* Recruitment impersonation

JobShield aims to provide users with an additional layer of verification by analyzing multiple signals associated with a job or internship opportunity.

---

# 🎯 Objective

The main objective of JobShield is to provide an **explainable risk assessment** rather than simply returning a binary "Fake" or "Real" result.

The system generates:

* Risk score
* Risk level
* Possible scam category
* Detected risk signals
* Supporting evidence
* Recommended safety actions

> **Note:** The generated score represents a system risk assessment and is not a guarantee that an opportunity is fraudulent.

---

# 🏗️ System Architecture

```text
                         USER
                           │
                           ▼
                    REACT FRONTEND
                           │
              ┌────────────┼────────────┐
              │            │            │
            Text        Screenshot      URL
              │            │            │
              │           OCR            │
              │            │            │
              └────────────┼────────────┘
                           ▼
                    FLASK BACKEND
                           │
                           ▼
                  INPUT PREPROCESSING
                           │
                           ▼
                    TEXT EXTRACTION
                           │
                           ▼
                     TEXT CLEANING
                           │
                           ▼
                 INFORMATION EXTRACTION
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
        Rule Detection   NLP/ML    Verification
              │            │            │
              │            │       ┌────┴────┐
              │            │       │         │
              │            │    Company   Recruiter
              │            │ Verification Verification
              │            │       │         │
              └────────────┼───────┴─────────┘
                           ▼
                    URL ANALYSIS
                           │
                           ▼
                 SCAM CLASSIFICATION
                           │
                           ▼
                  MULTI-SIGNAL RISK
                       ENGINE
                           │
                           ▼
                     RISK SCORE
                         0–100
                           │
                           ▼
                  EXPLAINABLE AI
                           │
                           ▼
                     EVIDENCE
                           │
                           ▼
                 SAFETY RECOMMENDATIONS
                           │
                           ▼
                   FINAL REPORT
                           │
                           ▼
                    REACT FRONTEND
                           │
                           ▼
                       USER
```

The project's complete workflow follows input submission → preprocessing → extraction → detection → verification → risk scoring → explanation → final report → feedback/database.

---

# 🔄 Complete Workflow

### 1. User Input

The user submits a job or internship opportunity through one of the available input methods:

```text
Job Description
Job URL
Recruiter Email
Recruiter Phone
Screenshot
PDF/Image
```

### 2. Input Preprocessing

The backend determines the type of input and selects the appropriate processing method.

```text
Text       → Direct processing
Screenshot → OCR
PDF        → Text extraction
URL        → Web/URL extraction
Email      → Email-domain extraction
```

### 3. OCR / Text Extraction

Screenshots and images are processed using OCR to convert visual content into machine-readable text.

### 4. Text Cleaning

Extracted text is normalized before NLP analysis.

Operations include:

* Lowercase conversion
* Symbol removal
* Duplicate-space removal
* Tokenization
* Irrelevant-word removal
* Normalization

### 5. Information Extraction

The system extracts important entities such as:

```text
Company
Job Title
Salary
Location
Experience
Skills
Internship Duration
Recruiter
Email
Phone
Website
Application URL
Payment Information
```

### 6. Rule-Based Detection

The system checks for suspicious patterns such as:

```text
Registration Fee
Security Deposit
Training Fee
Processing Fee
Pay to Apply
Guaranteed Job
Guaranteed Income
Urgent Application
Limited Seats
OTP
UPI PIN
Bank Details
```

### 7. NLP / Machine Learning

The cleaned job text is analyzed using an ML model.

The initial proposed approach is:

```text
Text
 ↓
TF-IDF
 ↓
Machine Learning Classifier
 ↓
Scam Probability
```

The project can begin with Logistic Regression and later experiment with other classifiers.

### 8. Company Verification

The system checks:

* Whether the claimed company exists
* Official company website
* Official careers page
* Company domain
* Advertised position
* Recruiter domain consistency

A domain mismatch is treated as a risk signal rather than automatic proof of fraud.

### 9. Recruiter Verification

The system analyzes:

* Recruiter email
* Email domain
* Phone number
* Company association
* Communication platform
* Claimed designation

### 10. URL Analysis

If a URL is provided, the system analyzes:

* HTTPS
* Domain
* URL structure
* Suspicious keywords
* URL shorteners
* Redirects
* Company/domain mismatch
* Suspicious domain patterns

### 11. Scam Classification

The system attempts to identify the possible scam category.

Possible categories include:

1. Upfront Payment Scam
2. Fake Recruiter
3. Fake Company
4. Fake Internship
5. Task Scam
6. Identity-Information Scam
7. Fake Work-from-Home Opportunity
8. Recruitment Impersonation
9. Suspicious Investment/MLM-style Opportunity
10. Other/Unknown

### 12. Multi-Signal Risk Engine

Multiple independent signals are combined:

```text
NLP Result
Payment Detection
Company Verification
Recruiter Verification
URL Analysis
Pattern Detection
OCR Analysis
Salary/Promise Analysis
```

The combined signals are processed by the Risk Engine.

### 13. Risk Score

The system generates a score between **0 and 100**.

|  Score | Risk Level |
| -----: | ---------- |
|   0–25 | Low Risk   |
|  26–50 | Caution    |
|  51–75 | Suspicious |
| 76–100 | High Risk  |

### 14. Explainable AI

Instead of displaying only the score, the system explains why the opportunity received the assessment.

Example:

```text
🔴 Upfront payment detected
🔴 Recruiter email does not match company domain
🔴 Unusually high salary claim
🟠 Urgency language detected
🟠 Company could not be independently verified
```

### 15. Evidence Generation

The system generates specific evidence supporting the detected signals.

```text
Evidence 1 → Payment requested
Evidence 2 → Recruiter domain mismatch
Evidence 3 → Company verification failed
Evidence 4 → Unusually high compensation claim
```

### 16. Final Report

The final report contains:

```text
Job Information
Risk Assessment
Scam Category
Detected Signals
Evidence
Recommended Actions
```

### 17. Feedback

Users can provide feedback on whether the assessment was useful or correct.

The feedback can be stored for future model improvement.

---

# 🖥️ Frontend

The frontend is responsible for user interaction and visualization.

### Main Screens

#### Home

```text
JOBSHIELD

Verify before you apply.

[ Paste Job ]

[ Upload Screenshot ]

[ Check URL ]

[ Check Recruiter ]
```

#### Analysis

```text
Analyzing opportunity...

✓ Text Analysis
✓ OCR Analysis
✓ Company Verification
✓ Recruiter Analysis
✓ URL Analysis
✓ Scam Pattern Analysis
```

#### Result

```text
🔴 HIGH RISK

87 / 100

Possible Scam:
Upfront Payment Scam

Detected Risks
• Payment requested
• Recruiter mismatch
• Urgency detected

Evidence
...

Recommended Actions
...
```

---

# ⚙️ Backend

The backend is built using **Python Flask** and acts as the central coordinator between the frontend and analysis modules.

### Proposed APIs

```text
POST /analyze/text
POST /analyze/screenshot
POST /analyze/url
POST /analyze/email

GET /report/<id>

POST /feedback
```

### Backend Responsibilities

```text
Receive Input
     ↓
Validate Request
     ↓
Preprocess Data
     ↓
Run Analysis Modules
     ↓
Generate Risk Signals
     ↓
Calculate Risk Score
     ↓
Generate Explanation
     ↓
Store Result
     ↓
Return JSON Response
```

---

# 🤖 Machine Learning

The initial ML pipeline uses:

```text
Dataset
   ↓
Text Cleaning
   ↓
Train/Test Split
   ↓
TF-IDF Vectorization
   ↓
ML Classifier
   ↓
Evaluation
   ↓
Saved Model
```

Possible classifiers:

* Logistic Regression
* Naive Bayes
* Random Forest
* SVM

The project will evaluate models using:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix
* ROC-AUC

---

# 📊 Dataset

The model requires examples of both legitimate and suspicious job opportunities.

### Legitimate Examples

* Real internships
* Graduate positions
* Work-from-home opportunities
* Genuine company postings

### Suspicious Examples

* Payment scams
* Fake recruiters
* Fake internships
* Task scams
* Identity theft scams
* Fake work-from-home jobs

Possible sources include:

* Kaggle
* Hugging Face
* Google Dataset Search
* Carefully constructed synthetic examples

---

# 🗄️ Database

The initial version uses **SQLite**.

### Jobs

```text
job_id
job_title
company
description
url
date_analyzed
```

### Analysis

```text
risk_score
risk_category
detected_signals
model_prediction
```

### Feedback

```text
job_id
user_feedback
timestamp
```

### Companies

```text
company_name
official_domain
verification_status
```

For deployment, the database can later be migrated to PostgreSQL.

---

# 🛠️ Technology Stack

| Component            | Technology               |
| -------------------- | ------------------------ |
| Frontend             | React                    |
| Styling              | HTML + CSS               |
| Backend              | Python Flask             |
| Database             | SQLite                   |
| ML                   | scikit-learn             |
| NLP                  | spaCy / NLTK             |
| OCR                  | Tesseract                |
| Image Processing     | OpenCV                   |
| PDF Extraction       | PyMuPDF                  |
| Web Extraction       | Requests + BeautifulSoup |
| Explainability       | SHAP / LIME              |
| Data Processing      | pandas                   |
| Numerical Processing | NumPy                    |
| API Testing          | Postman                  |
| Model Storage        | joblib                   |
| Version Control      | Git + GitHub             |

The project document specifies this overall stack.

---

# 📁 Project Structure

```text
JobShield/
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── README.md
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   │
│   ├── routes/
│   ├── preprocessing/
│   ├── nlp/
│   ├── detection/
│   ├── verification/
│   ├── risk/
│   ├── explainability/
│   ├── models/
│   └── database/
│
├── ml/
│   ├── dataset/
│   ├── notebooks/
│   ├── train.py
│   ├── evaluate.py
│   └── saved_models/
│
├── uploads/
│
├── docs/
│   ├── architecture/
│   ├── screenshots/
│   └── diagrams/
│
├── tests/
│
├── .gitignore
├── README.md
└── LICENSE
```

---

# 🚀 Getting Started

## Prerequisites

Install:

* Python 3.11
* Node.js
* Git
* VS Code

---

## Clone Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd JobShield
```

---

# 🐍 Backend Setup

```bash
cd backend
```

Create virtual environment:

```bash
python -m venv venv
```

Activate on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run Flask:

```bash
python app.py
```

Backend will run locally at:

```text
http://127.0.0.1:5000
```

---

# ⚛️ Frontend Setup

Open another terminal:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start development server:

```bash
npm run dev
```

---

# 🧪 API Testing

The backend APIs can be tested using Postman.

Example:

```text
POST /analyze/text
```

Request:

```json
{
    "text": "Congratulations! You are selected. Pay ₹1499 registration fee."
}
```

Example response:

```json
{
    "risk_score": 87,
    "risk_level": "High Risk",
    "scam_type": "Upfront Payment Scam",
    "signals": [
        "Payment request detected",
        "Urgency language detected"
    ]
}
```

---

# 🔐 Security & Privacy

Because users may upload screenshots containing personal information, the system should minimize unnecessary data storage.

The application should:

* Avoid storing unnecessary personal information
* Mask phone numbers where possible
* Mask email addresses where possible
* Delete uploaded screenshots when persistent storage is not required
* Never store passwords
* Never store OTPs
* Never store banking credentials
* Clearly communicate what information is stored

These privacy considerations are part of the project's design.

---

# 🧪 Testing

The system should be tested with multiple types of opportunities.

### Test Case 1 — Legitimate Internship

Expected:

```text
Low Risk
```

### Test Case 2 — Payment Scam

Expected:

```text
High Risk
```

### Test Case 3 — Fake Recruiter

Expected:

```text
Suspicious / High Risk
```

### Test Case 4 — Legitimate Company + Gmail Recruiter

Expected:

```text
Risk signal
```

but not automatically classified as fraudulent.

### Test Case 5 — Sophisticated Scam

The system should rely on multiple signals rather than only obvious scam keywords.

---

# 📈 Admin Dashboard

An optional admin dashboard can display:

* Total opportunities analyzed
* Suspicious opportunities
* High-risk opportunities
* Scam categories
* Model accuracy
* Precision
* Recall
* F1-score
* False positives
* False negatives

Possible charts:

```text
Risk Distribution
Scam Categories
Model Performance
Monthly Detections
```

---

# 🌐 Deployment

### Frontend

Possible platforms:

* Vercel
* Netlify

### Backend

Possible platforms:

* Render
* Railway
* Fly.io

### Database

Development:

```text
SQLite
```

Production:

```text
PostgreSQL
```

Docker can also be used for containerization.

---

# 👥 Team Contribution

Each team member can work on a separate module.

```text
Frontend
Backend
ML Model
OCR
Company Verification
Recruiter Verification
Database
Testing & Documentation
```

Recommended Git branches:

```text
main
frontend
backend
ml-model
ocr
verification
```

---

# 🗺️ Development Roadmap

### Phase 1 — Project Setup

* [ ] Create GitHub repository
* [ ] Set up frontend
* [ ] Set up Flask backend
* [ ] Configure SQLite
* [ ] Create API structure

### Phase 2 — Basic Detection

* [ ] Text input
* [ ] Text preprocessing
* [ ] Scam keyword detection
* [ ] Basic risk scoring
* [ ] Result dashboard

### Phase 3 — ML

* [ ] Collect dataset
* [ ] Clean dataset
* [ ] Train TF-IDF model
* [ ] Train classifier
* [ ] Evaluate model
* [ ] Save trained model

### Phase 4 — Multimodal Input

* [ ] Screenshot upload
* [ ] OCR
* [ ] PDF extraction
* [ ] URL extraction

### Phase 5 — Verification

* [ ] Company verification
* [ ] Recruiter verification
* [ ] Domain analysis
* [ ] URL analysis

### Phase 6 — Explainability

* [ ] Risk signals
* [ ] Evidence generation
* [ ] Explainable result
* [ ] Safety recommendations

### Phase 7 — Final System

* [ ] Feedback system
* [ ] Admin dashboard
* [ ] Testing
* [ ] Security/privacy
* [ ] Deployment
* [ ] Final documentation

---

# 📌 Disclaimer

JobShield is an experimental AI-assisted risk assessment system.

Its results should be treated as **risk indicators rather than definitive proof** that a job or internship is fraudulent.

Users should independently verify opportunities through official company websites and trusted communication channels before sharing sensitive information or making payments.

---

# 📚 Project Documentation

Additional project documentation will be maintained in:

```text
/docs
```

including:

* System architecture
* Database design
* API documentation
* ML documentation
* Flowcharts
* UML diagrams
* Testing documentation
* Screenshots
* Deployment documentation

---

# ⭐ Project Goal

> **Verify before you apply.**

JobShield aims to help students and job seekers identify potential warning signs in job and internship opportunities through a combination of AI, NLP, OCR, verification, and explainable risk analysis.
