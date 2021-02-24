import re as REGEX
import xml.etree.ElementTree as ET
import os
MyDir = os.getcwd()
def ListenFor(TEXT,PATTERN):
    TEXT_LOWER = TEXT.lower()
    if REGEX.search(PATTERN,TEXT_LOWER):
        return True
    else:
        return False
    
class Bot():
    def __init__(self):
        pass
    
    def get_response(self,text):
        os.chdir(MyDir)
        tree = ET.parse('training/convo.xml')
        root = tree.getroot()

        a = root[0]

        Responses = []
        for subelem in a:
            if ListenFor(text,subelem.attrib["input"]):
                Response = subelem.text
                Responses.append(Response)
        return Responses
            
