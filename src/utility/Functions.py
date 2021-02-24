import speech_recognition as RECOGNITION_MODULE
import re as REGEX
import playsound as PLAY_SOUND
from gtts import gTTS
import xml.etree.ElementTree as ET
import os
import importlib
import pyfiglet
import threading
from utility import Settings as sets
import time
import sys

RECOGNIZER = RECOGNITION_MODULE.Recognizer()
MyDir = os.getcwd()
TimeLog1_ = time.time()
LastSpeakTime = 0
COLORS = {\
    "black":"\u001b[30;1m",
    "red": "\u001b[31;1m",
    "green":"\u001b[32m",
    "yellow":"\u001b[33;1m",
    "blue":"\u001b[34;1m",
    "magenta":"\u001b[35m",
    "cyan": "\u001b[36m",
    "white":"\u001b[37m",
    "yellow-background":"\u001b[43m",
    "black-background":"\u001b[40m",
    "cyan-background":"\u001b[46;1m",
    }
    
def colorText(text):
    for color in COLORS:
        text = text.replace("[["+color+"]]",COLORS[color])
    return text

def Listen(TIME):
    RETURN_VALUE = ""
    with RECOGNITION_MODULE.Microphone() as MIC_OUTPUT:
        try:
            VOICE_AUDIO = RECOGNIZER.record(MIC_OUTPUT,TIME)
            REAL_TEXT = RECOGNIZER.recognize_google(VOICE_AUDIO)
            RETURN_VALUE = REAL_TEXT
            sets.LastMe = RETURN_VALUE
        except Exception as e:
            print(e)
    log = open("misc/logs/chat_logs.txt","a")
    log.write("\n"+sets.user+": "+RETURN_VALUE)
    log.close()
    return RETURN_VALUE

def ListenForever():
    RETURN_VALUE = ""
    with RECOGNITION_MODULE.Microphone() as MIC_OUTPUT:
        try:
            VOICE_AUDIO = RECOGNIZER.listen(MIC_OUTPUT)
            REAL_TEXT = RECOGNIZER.recognize_google(VOICE_AUDIO)
            RETURN_VALUE = REAL_TEXT
            sets.LastMe = RETURN_VALUE
        except:
            print(5)
            
    log = open("misc/logs/chat_logs.txt","a")
    log.write("\n"+sets.user+": "+RETURN_VALUE)
    log.close()
    return RETURN_VALUE

def ListenFor(TEXT,PATTERN):
    TEXT_LOWER = TEXT.lower()
    if REGEX.search(PATTERN,TEXT_LOWER):
        return True
    else:
        return False

def PlaySound(location):
    #PLAY_SOUND.playsound("crab.mp3",False)
    os.system(location)

def newprint(value,add,Targeting):
    if Targeting:
        os.system("cls")
        pyfiglet.print_figlet("BMO",colors="CYAN")
        print(colorText(add+value))
    #log = open("log.txt","a")
    #log.write("\n"+sets.user+": "+value)
    #log.close()
    
def Speak(Text):
    os.chdir(MyDir)
    pyfiglet.print_figlet(Text,colors="RED")
    log = open("misc/logs/chat_logs.txt","a")
    log.write("\nBMO: "+Text)
    log.close()
    TimeLog1_ = time.time()
    TTS = gTTS(text=Text,lang="en")
    TTS.save("VOICE.mp3")
    PLAY_SOUND.playsound("VOICE.mp3")
    os.remove("VOICE.mp3")
    LastSpeakTime = time.time() - TimeLog1_
    sets.Latency = LastSpeakTime
    sets.LastBot = Text

def ProcessCommand(Text,Commands):
    RUNNING = True
    for name in Commands:
        cmdclass = Commands[name]
        for arg in cmdclass.aliases:
            if ListenFor(Text,arg):
                successful = cmdclass.run()
                return successful
    Speak("Unrecognised Command")
    RUNNING = False

def AttemptLogin(AUTH):
    os.chdir(MyDir)
    tree = ET.parse('training/convo.xml')
    root = tree.getroot()

    sets.user = "Testing"
    sets.LoggedIn = True
    return True
    a = root[1]
    for subelem in a:
        if ListenFor(AUTH,subelem.attrib["name"]):
            Name = subelem.text
            sets.LoggedIn = True
            sets.user = Name
            return True
    return False
