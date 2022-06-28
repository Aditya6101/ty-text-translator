from gtts import gTTS
from playsound import playsound
import os

# importing custom module
import lang
import translate

# prompt user to enter the text to be converted
text_to_convert = """Il tramonto è l'ora del giorno in cui il nostro cielo incontra i venti solari dello spazio esterno."""


# detect the language of entered text
from_language = lang.detect_language(text_to_convert)
to_language = 'tr'

# convert the text to english
text_to_read = translate.translate_text(
    text_to_convert, from_language, to_language)
text = text_to_read.text

print(text_to_convert)
print(text)

obj = gTTS(text=text, lang=to_language, slow=False, tld="co.in")

obj.save("speech.mp3")

playsound("speech.mp3", True)

os.remove("speech.mp3")
