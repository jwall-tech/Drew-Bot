import os
import sys
import time
import requests

class Updater():
    def __init__(self,url,filename):
        self.url = url
        self.filename = filename

    def Update(self):
        canUpdate = self._canupdate()
        if canUpdate:
            print("UPDATING")
            testPath = self._parselink(["src","drewcore.py"])
        else:
            print("LATEST VERSION")
            return False

    def _canupdate(self):
        check = requests.get(self.url+"/master/"+self.filename)
        if check.status_code == 200:
            myVers = open("../version.txt","r")
            lines = myVers.readlines()
            Vers = lines[0]
            if float(Vers.split(":")[1]) < float(check.text.split(":")[1]):
                print("FOUND VERSION "+check.text)
                return True
        return False

    def _parselink(self,locationtable):
        currentPath = self.url + "/master"
        myDir = os.getcwd()
        os.chdir("../")

        for item in locationtable:
            if os.path.isdir(currentPath+"/"+item):
                currentPath = currentPath + "/" + item
            else:
                currentPath = currentPath + "/" + item

        print(currentPath)
        os.chdir(myDir)
        return currentPath
