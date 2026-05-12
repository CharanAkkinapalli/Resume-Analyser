import streamlit as st
from utils.text_processing import extract_text
from utils.keyword_check import check_keywords
from utils.ats_checker import ats_check
import textstat
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# --- Header ---
st.title("📄 AI-Powered Resume Analyzer")
st.markdown("Upload your resume and get **personalized insights** into strengths and areas to improve.")

# --- Inputs ---
uploaded_file = st.file_uploader("Upload your resume (PDF/TXT)", type=["pdf", "txt"])
job_desc = st.text_area("Paste a job description (optional)")

if uploaded_file:
    resume_text = extract_text(uploaded_file)

    # Resume preview
    st.subheader("📝 Resume Text Preview")
    st.write(resume_text[:500] + "..." if len(resume_text) > 500 else resume_text)

    # --- Keyword Coverage ---
    st.subheader("🔑 Keyword Coverage")
    keywords = ["Python", "Java", "SQL", "Machine Learning", "Leadership"]
    coverage = check_keywords(resume_text, keywords)

    cols = st.columns(len(coverage))
    for i, (kw, present) in enumerate(coverage.items()):
        if present:
            cols[i].success(f"✔ {kw}")
        else:
            cols[i].warning(f"⚠ {kw}")

    # --- Readability Scores ---
    st.subheader("📖 Readability Scores")
    col1, col2, col3 = st.columns(3)
    col1.metric("Flesch Reading Ease", f"{textstat.flesch_reading_ease(resume_text):.2f}")
    col2.metric("Grade Level", f"{textstat.flesch_kincaid_grade(resume_text):.2f}")
    col3.metric("Reading Time", f"{textstat.reading_time(resume_text):.1f} mins")

    # --- ATS Compatibility ---
    st.subheader("⚡ ATS Compatibility")
    warnings = ats_check(resume_text)
    for warning in warnings:
        if "No major" in warning:
            st.success(warning)
        else:
            st.error(warning)

    # --- Job Description Match ---
    if job_desc:
        vectorizer = TfidfVectorizer().fit([resume_text, job_desc])
        vectors = vectorizer.transform([resume_text, job_desc])
        similarity = cosine_similarity(vectors[0], vectors[1])[0][0] * 100

        st.subheader("🎯 Job Description Match")
        st.progress(similarity / 100.0)
        st.write(f"Match Score: **{similarity:.2f}%**")

    # --- Summary Section ---
    st.markdown("### 🌟 Summary")
    strengths = [kw for kw, present in coverage.items() if present]
    weaknesses = [kw for kw, present in coverage.items() if not present]

    summary_text = f"Your resume shows strong skills in **{', '.join(strengths)}**."
    if weaknesses:
        summary_text += f" To make it even stronger, add more detail on **{', '.join(weaknesses)}**."
    summary_text += " Aim for Grade Level 10–12 for better readability."

    st.info(summary_text)