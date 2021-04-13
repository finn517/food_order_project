"""Interacts with user by using google text to speech
code written by Finn Cook G01134138"""
from gtts import gTTS
import os
import playsound

def speak(text):
    tts = gTTS(text=text, lang='es')
    filename = 'voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)
    os.remove('voice.mp3')
#speak("Por favor ingrese los datos que se pediran")


