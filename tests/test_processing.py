import io
import pytest
from utils.text_processing import extract_text
from utils.keyword_check import check_keywords
from utils.ats_checker import ats_check

def test_extract_text_txt():
    # Simulate a text file upload
    fake_file = io.BytesIO(b"Hello, this is a sample resume with Python and SQL skills.")
    fake_file.name = "resume.txt"
    result = extract_text(fake_file)
    assert "Python" in result
    assert "SQL" in result

def test_check_keywords():
    text = "Experienced in Python, SQL, and Machine Learning."
    keywords = ["Python", "Java", "SQL"]
    result = check_keywords(text, keywords)
    assert result["Python"] is True
    assert result["SQL"] is True
    assert result["Java"] is False

def test_ats_check_short_resume():
    text = "Short resume text"
    warnings = ats_check(text)
    assert any("too short" in w.lower() for w in warnings)

def test_ats_check_missing_sections():
    text = "This resume only mentions hobbies."
    warnings = ats_check(text)
    assert any("missing standard sections" in w.lower() for w in warnings)

def test_ats_check_no_issues():
    text = (
        "Education: B.Tech in Computer Science\n"
        "Experience: 2 years as Software Engineer\n"
        "Skills: Python, SQL, Machine Learning, Leadership\n"
        "Projects: Built Resume Analyzer, Library Management System\n"
        "Achievements: Published research paper, won hackathon"
    )
    warnings = ats_check(text, min_words=20)  # Lower threshold for testing
    assert "No major ATS issues detected." in warnings