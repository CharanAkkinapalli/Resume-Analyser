import PyPDF2

def extract_text(uploaded_file):
    """
    Extract text from uploaded resume file.
    Supports Streamlit UploadedFile (with .type) and raw BytesIO (used in tests).
    """
    file_type = getattr(uploaded_file, "type", None)
    file_name = getattr(uploaded_file, "name", "")

    # Handle PDF files
    if file_type == "application/pdf" or file_name.endswith(".pdf"):
        reader = PyPDF2.PdfReader(uploaded_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text

    # Handle text files
    content = uploaded_file.read()
    if isinstance(content, bytes):
        return content.decode("utf-8")
    return str(content)