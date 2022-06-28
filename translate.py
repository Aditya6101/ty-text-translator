from googletrans import Translator

translator = Translator()


def translate_text(text, from_language, to_language):
    translated_text = translator.translate(
        text, src=from_language, dest=to_language)
    return translated_text
