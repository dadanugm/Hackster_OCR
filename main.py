import pyttsx3
from gtts import gTTS
from io import BytesIO
import os
from playsound import playsound

synthesizer = pyttsx3.init()
synthesizer.setProperty('rate', 100)
synthesizer.say("tes satu dua tiga")
synthesizer.runAndWait()
synthesizer.stop()

'''
mp3_fp = BytesIO()
tts = gTTS('tes satu dua tiga', lang='en')
tts.write_to_fp(mp3_fp)
'''
'''
tts = gTTS('test satu dua tiga empat lima enam', lang='id')
tts.save('hello.mp3')
playsound('hello.mp3')
'''