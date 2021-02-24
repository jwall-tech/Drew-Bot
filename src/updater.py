import os
import sys
import time
import requests

class Updater():
    def __init__(self,url,filename):
        self.url = url
        self.filename = filename

    def Update(self):
        pass

    def _canupdate(self):
        test = requests.get(self.url)
        return test
    
    def _getversion(self):
        pass

    def _doupdate(self):
        pass
