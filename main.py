from gtts import gTTS
from playsound import playsound
import os

text_val = """Hey Aditya, What's up dude?"""

language = 'en'

obj = gTTS(text=text_val, lang=language, slow=False, tld="co.in")

obj.save("speech.mp3")

playsound("speech.mp3")

os.remove("speech.mp3")
