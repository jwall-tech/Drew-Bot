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
        self.ID = "HideUI"
        self.aliases = ["tango","hide","hide ui","hide u i","hide g u i","hide gui","hide interface","hide panel","hide panell"]

    def run(self):
        sets.UI_HIDDEN = True
def Setup():
    CMD = Command()
    return CMD
