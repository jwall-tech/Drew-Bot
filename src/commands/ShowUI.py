from _Funcs import *
import time
import speech_recognition as RECOGNITION_MODULE
import re as REGEX
import playsound as PLAY_SOUND
from gtts import gTTS
import sys
import os
myDir = os.getcwd()
os.chdir("../")
from utility import Settings as sets
os.chdir(myDir)

class Command():
    def __init__(self):
        self.ID = "ShowUI"
        self.aliases = ["orange","show","show ui","show u i","show g u i","show gui","show interface","show panel","show panell"]

    def run(self):
        sets.UI_HIDDEN = False
def Setup():
    CMD = Command()
    return CMD
