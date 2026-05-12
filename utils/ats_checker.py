def ats_check(text, min_words=50):
    """
    Check resume text for ATS compatibility issues.
    Default minimum word count is 50 (adjustable).
    """
    warnings = []
    words = text.split()

    if len(words) < min_words:
        warnings.append("Resume seems too short — may lack detail.")
    if "table" in text.lower() or "graphic" in text.lower():
        warnings.append("Avoid tables/graphics — ATS may not parse them.")
    if not any(section in text.lower() for section in ["education", "experience", "skills"]):
        warnings.append("Missing standard sections (Education/Experience/Skills).")

    return warnings if warnings else ["No major ATS issues detected."]