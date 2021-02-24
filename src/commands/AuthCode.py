from _Funcs import *
import time
import speech_recognition as RECOGNITION_MODULE
import re as REGEX
import playsound as PLAY_SOUND
from gtts import gTTS
import xml.etree.ElementTree as ET
import sys
import os
myDir = os.getcwd()
os.chdir("../")
from utility import Settings as sets
os.chdir(myDir)

class Command():
    def __init__(self):
        self.ID = "AuthCode"
        self.aliases = ["new auth","new code","new account","make auth"]

    def run(self):
        Speak("What is the auth code you want to create?")
        AuthCode = ListenForever()
        Speak("Is this right, "+AuthCode)
        Confirm = ListenForever()
        if REGEX.search("yes",Confirm.lower()):
            Speak("What is this users name?")
            Name = ListenForever()
            Speak("Okay, so you want to create an auth code for "+Name+" with the code "+AuthCode)
            ConfirmTwo = ListenForever()
            if REGEX.search("yes",ConfirmTwo.lower()):
                tree = ET.parse("chats.xml")
                xmlRoot = tree.getroot()
                myRoot = xmlRoot[1]

                child = ET.Element("auth_code",name=AuthCode)
                child.text = Name
                myRoot.append(child)
                tree.write("chats.xml")

            else:
                self.run()
        else:
            self.run()
def Setup():
    CMD = Command()
    return CMD


