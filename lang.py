from langdetect import detect


def detect_language(text):
    detected_lang = detect(text)
    return detected_lang
