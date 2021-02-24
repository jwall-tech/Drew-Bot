from _Funcs import *
import time
import speech_recognition as RECOGNITION_MODULE
import re as REGEX
import playsound as PLAY_SOUND
from gtts import gTTS
import sys
import os
import webbrowser
class Command():
    def __init__(self):
        self.ID = "Web"
        self.aliases = ["search","find"]

    def run(self):
        Speak("What do you want me to search for?")
        SearchFor = ListenForever()
        webbrowser.open("https://en.wikipedia.org/wiki/"+SearchFor)
        Speak("Here is a wikipedia article on "+SearchFor)
def Setup():
    CMD = Command()
    return CMD
