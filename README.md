# AI Resume Analyzer & Job Matcher

AI Resume Analyzer & Job Matcher is a web-based application that analyzes a candidate's resume and matches it with available job descriptions using Natural Language Processing (NLP) techniques.

The system extracts text from resumes, compares it with job descriptions using TF-IDF and Cosine Similarity, and recommends the most suitable job roles based on match scores.

---

## Features

• Upload and analyze resumes in PDF format  
• Automatic resume text extraction  
• Candidate name detection from resume  
• Resume–Job Description matching using TF-IDF and Cosine Similarity  
• Match score calculation for multiple job roles  
• Dashboard showing analytics and match scores  
• Job listing panel displaying available job roles  

---

## Tech Stack

### Backend
- Django
- Django REST Framework

### Machine Learning / NLP
- Scikit-learn
- TF-IDF Vectorizer
- Cosine Similarity

### Frontend
- HTML
- CSS
- JavaScript
- Chart.js

### Libraries
- PyMuPDF (fitz) for PDF text extraction

---

## Project Workflow

Resume Upload  
↓  
PDF Text Extraction  
↓  
Resume Parsing  
↓  
TF-IDF Vectorization  
↓  
Cosine Similarity Matching  
↓  
Job Match Score Calculation  
↓  
Dashboard Analytics

---




## Installation


## Clone the repository
git clone https://github.com/sakshimote20/AI-Resume-Analyzer-Job-Matcher.git


## Navigate to the project folder
cd resume_analyzer


## Install dependencies
pip install -r requirements.txt


## Run database migrations
python manage.py migrate


## Start the development server
python manage.py runserver


## Open in browser
http://127.0.0.1:8000


---

## Future Improvements

• Resume skill extraction using advanced NLP  
• ATS resume scoring system (0–100)  
• Intelligent job recommendation system  
• Candidate login and recruiter dashboard  
• Resume history tracking  

---
