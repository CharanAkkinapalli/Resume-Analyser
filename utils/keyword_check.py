def check_keywords(text, keywords):
    text_lower = text.lower()
    results = {}
    for kw in keywords:
        results[kw] = kw.lower() in text_lower
    return results