from _Funcs import *
import time
import speech_recognition as RECOGNITION_MODULE
import re as REGEX
import playsound as PLAY_SOUND
from gtts import gTTS
import sys
import os

class Command():
    def __init__(self):
        self.ID = "BaseCMD"
        self.aliases = []

    def run(self):
        #Do the command actions here
        pass
def Setup():
    CMD = Command()
    return CMD
