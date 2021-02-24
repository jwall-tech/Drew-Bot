import os
#from BMO.MK4 import Sets as sets
import time
import speech_recognition as RECOGNITION_MODULE
import re as REGEX
import playsound as PLAY_SOUND
from gtts import gTTS
RECOGNIZER = RECOGNITION_MODULE.Recognizer()
wd = os.getcwd()
myDir = os.getcwd()
os.chdir("../")
from utility import Settings as sets
os.chdir(myDir)
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
import pyfiglet

def colorText(text):
    for color in COLORS:
        text = text.replace("[["+color+"]]",COLORS[color])
    return text

def Speak(Text):
    pyfiglet.print_figlet(Text,colors="RED")
    TTS = gTTS(text=Text,lang="en")
    TTS.save("test.mp3")
    PLAY_SOUND.playsound("test.mp3")
    os.remove("test.mp3")
    log = open("log.txt","a")
    log.write("\nBMO: "+Text)
    log.close()

def PlaySound(location):
    os.system(location)

def ListenFor(TEXT,PATTERN):
    TEXT_LOWER = TEXT.lower()
    if REGEX.search(PATTERN,TEXT_LOWER):
        return True
    else:
        return False
    
def newprint(value,add):
    os.system("cls")
    pyfiglet.print_figlet("BMO",colors="CYAN")
    print(colorText(add+value))
    
def Listen(TIME):
    print("TALK")
    RETURN_VALUE = ""
    with RECOGNITION_MODULE.Microphone() as MIC_OUTPUT:
        try:
            VOICE_AUDIO = RECOGNIZER.record(MIC_OUTPUT,TIME)
            REAL_TEXT = RECOGNIZER.recognize_google(VOICE_AUDIO)
            RETURN_VALUE = REAL_TEXT
        except:
            pass
    log = open("log.txt","a")
    log.write("\n"+sets.user+"_: "+RETURN_VALUE)
    log.close()
    print("STOP TALKING")
    return RETURN_VALUE

def ListenForever():
    print("TALK")
    RETURN_VALUE = ""
    with RECOGNITION_MODULE.Microphone() as MIC_OUTPUT:
        try:
            VOICE_AUDIO = RECOGNIZER.listen(MIC_OUTPUT)
            REAL_TEXT = RECOGNIZER.recognize_google(VOICE_AUDIO)
            RETURN_VALUE = REAL_TEXT
        except:
            pass
    log = open("log.txt","a")
    log.write("\n"+sets.user+"_: "+RETURN_VALUE)
    log.close()
    print("STOP TALKING")
    return RETURN_VALUE

def GetAssetLocation(FolderName):
    os.chdir("Assets/"+FolderName)

def ReturnLocation():
    os.chdir(wd)
