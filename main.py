from gtts import gTTS
from playsound import playsound
import os

# importing custom module
import lang

# prompt user to enter the text to be converted
text = """DALL·E[1]
We decided to name our model using a portmanteau of the artist Salvador Dalí and Pixar’s WALL·E. is a 12-billion parameter version of GPT-3 trained to generate images from text descriptions, using a dataset of text–image pairs. We’ve found that it has a diverse set of capabilities, including creating anthropomorphized versions of animals and objects, combining unrelated concepts in plausible ways, rendering text, and applying transformations to existing images."""

# detect the language of entered text
language = lang.detect_language(text)

obj = gTTS(text=text, lang=language, slow=False, tld="co.in")

obj.save("speech.mp3")

playsound("speech.mp3", True)

os.remove("speech.mp3")
