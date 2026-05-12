📄 AI-Powered Resume Analyzer

🚀 Live Demo
Try it here: [Resume Analyzer App](https://resume-analyser-kgavgwc2akthjacyjcdae3.streamlit.app/)

🔍 Overview
The Resume Analyzer is a Streamlit web app that helps job seekers evaluate their resumes for **ATS compatibility, keyword coverage, readability, and job description match**. It provides actionable insights so you can strengthen your resume and improve your chances of landing interviews.

✨ Features
- "Keyword Coverage": Check if your resume includes critical skills (e.g., Python, SQL, Machine Learning).
- "Readability Scores": Evaluate clarity with Flesch Reading Ease, Grade Level, and estimated reading time.
- "ATS Compatibility": Detect formatting issues and missing sections that may confuse Applicant Tracking Systems.
- "Job Description Match": Compare your resume against a pasted job description using TF‑IDF similarity.
- "Friendly Feedback": Highlights strengths and suggests improvements in plain language.

🛠️ Tech Stack
- "Frontend/UI": Streamlit  
- "Backend/Logic": Python  
- "Libraries":  
  - `textstat` for readability  
  - `PyPDF2` for PDF parsing  
  - `scikit-learn` for similarity scoring  
  - `nltk` / `spacy` for NLP  
- "Testing": pytest  

---

📂 Project Structure
Resume-Analyser/
│
├── app.py                # Your Streamlit app
├── requirements.txt      # Dependencies
├── README.md             # Project documentation
├── utils/                # Helper scripts
│   ├── text_processing.py
│   ├── keyword_check.py
│   └── ats_checker.py
├── tests/                # Unit tests
│   └── test_processing.py
└── assets/               # (optional) screenshots/demo images


⚡ Quick Start

1. Clone the repo

    git clone https://github.com/<your-username>/resume-analyser.git
    cd resume-analyser

2. Install dependencies
    python -m pip install -r requirements.txt

3. Run the app
    python -m streamlit run app.py

4. Run tests
    python -m pytest tests/
    
⚒️Future Improvements
- Support for DOCX resumes
- Advanced NLP (BERT embeddings for similarity)
- Automated resume improvement suggestions
