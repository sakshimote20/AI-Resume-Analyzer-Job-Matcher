# 🤖 AI Resume Analyzer & Job Matcher

AI Resume Analyzer & Job Matcher is a web-based application that analyzes a candidate’s resume and matches it with available job descriptions using Natural Language Processing (NLP).

The system extracts text from resumes, compares it with job descriptions using **TF-IDF and Cosine Similarity**, and calculates match scores to recommend the most suitable job roles.

Built using **Django, Django REST Framework, Scikit-learn, HTML/CSS, JavaScript, and Chart.js**.

---

## 🚀 Features

- 📄 **Resume Upload**: Upload resumes in PDF format
- 🔍 **Automatic Text Extraction**: Extracts resume text using PyMuPDF
- 🧑 **Candidate Name Detection**: Automatically detects candidate name from resume
- 🤖 **AI Job Matching**: Uses TF-IDF and Cosine Similarity to match resumes with job descriptions
- 📊 **Match Score Visualization**: Displays job match scores through analytics charts
- 💼 **Job Listings Panel**: Shows available job roles from the database
- 📈 **Dashboard Interface**: Interactive UI to view results and analytics

---

## 🧠 Tech Stack

| Tool / Library | Purpose |
|----------------|--------|
| Django | Backend Web Framework |
| Django REST Framework | API Development |
| Scikit-learn | TF-IDF Vectorization & Cosine Similarity |
| PyMuPDF (fitz) | Resume PDF Text Extraction |
| HTML, CSS, JavaScript | Frontend |
| Chart.js | Analytics Visualization |
| SQLite  | Database |

---


## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/sakshimote20/AI-Resume-Analyzer-Job-Matcher.git
cd resume_analyzer
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run database migrations

```bash
python manage.py migrate
```

### 4️⃣ Start the development server

```bash
python manage.py runserver
```

### 5️⃣ Open in browser

```
http://127.0.0.1:8000
```

---

## 📊 How It Works

Resume Upload  
↓  
PDF Text Extraction (PyMuPDF)  
↓  
Resume Parsing  
↓  
TF-IDF Vectorization  
↓  
Cosine Similarity Matching  
↓  
Job Match Score Calculation  
↓  
Dashboard Visualization

---


## 🔮 Future Improvements

- 🔍 Advanced NLP skill extraction
- ⭐ ATS Resume Score (0–100)
- 💡 Intelligent job recommendation engine
- 👤 Candidate login system
- 📊 Resume history tracking

---

## 👩‍💻 Author

**Sakshi Mote**  
Final Year B.E. Artificial Intelligence & Data Science  
Dr. D. Y. Patil College of Engineering, Pune  

GitHub:  
https://github.com/sakshimote20
