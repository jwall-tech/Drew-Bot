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
            os.system("cls")
            print("UPDATING "+canUpdate[0])
            startTable = []
            start = "../src"
            vfile = open("../version.txt","w")
            print(canUpdate[0])
            vfile.write(canUpdate[0])
            vfile.close()
            os.system("color 2")
            def searchFolder(start):
                for file in os.listdir(start):
                    location = start + "/" +file
                    if not file.startswith("__"):
                        if os.path.isdir(location):
                            print("Searching Folder "+file+"\n")
                            searchFolder(location)
                        else:
                            locationT = []
                            for item in location.split("/"):
                                if not item.startswith(".."):
                                    locationT.append(item)
                            fileLink = self._parselink(locationT)
                            print("Getting File "+file+" from "+fileLink+"\n")
                            gfile = requests.get(fileLink)
                            print("Writing New Contents from "+file+" to "+location)
                            try:
                                temp = open(location,"w")
                                temp.write(gfile.text)
                                temp.close()
                                print("Updated file "+file)
                            except Exception as e:
                                print("Error Writing to file "+file)
                                print(e)
            searchFolder(start)
            input("RESTART DREW")
            exit()
        else:
            print("LATEST VERSION")
            return False

    def _canupdate(self):
        check = requests.get(self.url+"/master/"+self.filename)
        if check.status_code == 200:
            myVers = open("../version.txt","r")
            lines = myVers.readlines()
            myVers.close()
            Vers = lines[0]
            if float(Vers.split(":")[1]) < float(check.text.split(":")[1]):
                print("FOUND VERSION "+check.text)
                return [check.text,True]
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

        os.chdir(myDir)
        return currentPath
