import google.generativeai  as genai
import PIL.Image
import re
from gtts import gTTS
from io import BytesIO

from IPython.display import Audio
from playsound import playsound


genai.configure(api_key="AIzaSyC9QcNaPRuBO1Nlgw2PehEUv9vmXnLC1zU")

model=genai.GenerativeModel("gemini-pro-vision")

img=PIL.Image.open("./test-images/test3.jpeg")

response=model.generate_content(["Identify the IC just tell me what is the general name of it and list some 5 applications of it",img])


def to_plain_text(text):
    return re.sub(r"[^\w\s]","",text)


plain_text=to_plain_text(response.text)

text_to_speech=gTTS(text=plain_text,lang="en",tld="co.in",slow=False)

text_to_speech.save("./res.mp3")

audio_file = './res.mp3'

playsound(audio_file)