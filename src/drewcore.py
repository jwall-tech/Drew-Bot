## Bots / AI
from chatbot import ChatBot
import discord as DiscordBot

## Core
import databases as Databases
import interface as Interface
import utility as Util
from utility.Functions import *
import webserver as WebServer
from updater import Updater as UpdateChecker

## System
import os
import sys
import time

## External
import speech_recognition as SpeechRecog
import re as RegularEx
from gtts import gTTS as TextToSpeech
import xml.etree.ElementTree as XmlParser
import importlib
import pyfiglet
import threading
import playsound as PlaySound

## Setup Variables
GithubURL = "https://raw.githubusercontent.com/attroxide/Drew-Bot"
Updater = UpdateChecker(GithubURL,"version.txt")
Chatter = ChatBot.Bot()

# Check for update
UpdateCheck = Updater._canupdate()
if UpdateCheck:
    yn = input("An update was found, do you want to update?")
    if yn.lower() == "yes":
        Updater.Update()

## Run Function
def BotRuntime():
    # Runtime Variables
    MyDir = os.getcwd()
    CurrentTick = time.time()
    LastSpeakTick = 0
    Bot_LoggedIn = False
    Bot_Running = False
    Bot_Targeting = False

    # Commands
    LoadedCommands = {}

    # Command Prompt Setup
    os.system("cls")
    os.system("title Drew")
    DrewArt = pyfiglet.print_figlet("Drew",colors="CYAN")

    # Command Log Setup
    logFile = open("misc/logs/chat_logs.txt","w")
    logFile.close()
    
    # Command Loader
    for Temp_Command in os.listdir("commands"):
        if not Temp_Command.startswith("_"):
            sys.path.insert(0,"commands")
            module_import = importlib.import_module(Temp_Command[:len(Temp_Command)-3])
            module_class = module_import.Setup()
            LoadedCommands[module_class.ID] = module_class

    # Main Loop
    while True:
        # Setup
        Bot_LoggedIn = Util.Settings.LoggedIn

        # Get Speech
        PossibleChat = ListenForever()

        # Print
        newprint("You: "+PossibleChat,"[[cyan]]",Bot_Targeting)

        #Activation Check
        if ListenFor(PossibleChat,"hey drew") or ListenFor(PossibleChat,"drew"):
            Bot_Targeting = True
            Speak("How can I help?") 

        #Main Checks
        if not Bot_Running and Bot_Targeting:
            # Login
            if ListenFor(PossibleChat,"login") and not Bot_LoggedIn:
                Speak("What is your auth code?")
                PossibleCode = ListenForever()
                os.chdir(MyDir)
                Util.Settings.LoggedIn = True
                Util.Settings.user = "Test"
                Bot_LoggedIn = True
                Speak("Welcome back, "+Util.Settings.user)
                Targeting = False

            # Run Command
            elif ListenFor(PossibleChat,"command"):
                if Bot_LoggedIn:
                    Speak("What is your command, "+Util.Settings.user)
                    NewCommand = ListenForever()
                    Process = ProcessCommand(NewCommand,LoadedCommands)
                else:
                    Speak("You are not authorised to run commands")

            # Log Out
            elif ListenFor(PossibleChat,"quit") or ListenFor(PossibleChat,"log out"):
                if Bot_LoggedIn:
                    Bot_LoggedIn = False
                    Util.Settings.LoggedIn = False
                    Speak("Goodbye, "+Util.Settngs.user)
                else:
                    Speak("You are already logged out")
                Targeting = False

            # Chat
            else:
                Responses = Chatter.get_response(PossibleChat)
                if Responses:
                    for Response in Responses:
                        Speak(Response)
BotRuntime()
