import kivy
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
import Sets as settings
import threading
import Functions as func
from kivy.properties import ObjectProperty
import time

class Main(Screen):
    submit = ObjectProperty(None)
    auth_code = ObjectProperty(None)
    
    def login(self):
        code = self.auth_code.text
        success = func.AttemptLogin(code)
        if success:
            self.auth_code.text = ""
            sm.current = "debug"
            func.Speak("Welcome back, "+settings.user)
            LoggedIn = True
        else:
            func.Speak("Wrong Auth")

class CommandScreen(Screen):
    pass

class DebugScreen(Screen):
    latency = ObjectProperty(None)
    mespeak = ObjectProperty(None)
    botspeak = ObjectProperty(None)
    
class SettingScreen(Screen):
    pass

class AccountScreen(Screen):
    pass

class Manager(ScreenManager):
    pass

mainKv = Builder.load_file("ui/main.kv")
sm = Manager()
screens = [Main(),CommandScreen(),SettingScreen(),DebugScreen(),AccountScreen()]
for screen in screens:
    sm.add_widget(screen)
    
sm.current = "main"
LoggedIn = False
Hidden = False

class App(App):
    def __init__(self):
        super().__init__()
        
        def RunTime():
            Logged_In = LoggedIn
            HIDDEN = Hidden
            while True:
                time.sleep(0.5)
                if settings.UI_HIDDEN:
                    if not HIDDEN:
                        HIDDEN = True
                        pass
                else:
                    if HIDDEN:
                        HIDDEN = False
                        pass
                        
                if settings.LoggedIn:
                    if not Logged_In:
                        Logged_In = True
                        sm.current = "debug"
                else:
                    if Logged_In:
                        Logged_In = False
                        sm.current = "main"

                ds = screens[3]
                ds.latency.text = "Latency: "+str(settings.Latency)
                ds.mespeak.text = "Me: "+settings.LastMe
                ds.botspeak.text = "Bot: "+settings.LastBot
                    
        x = threading.Thread(target=RunTime)
        x.start()
        
    def build(self):
        sm.current = "main"
        self.title = 'CBB Assistant'
        return sm

    def logout(self):
        if settings.LoggedIn:
            settings.LoggedIn = False
            LoggedIn = False
            sm.current = "main"
            func.Speak("Goodbye")
        else:
            func.Speak("You are already logged out")
