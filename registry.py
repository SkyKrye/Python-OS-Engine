# registry.py

from os import *
import os

variables = {
    #---main
    "terminal": "standardTerminal",
    "username": "defaultUser",
    "password": "iJRJHGEYBV",
    "regcheck": "hi!!!!!",
    "username": os.getlogin(),
    "terminal": 'standardTerminal',
    "password": 'iJRJHGEYBV',
    "echo": 'iJRJHGEYBV',
    #---custom command module
    "command1": 'Command 1',
    "command2": 'Command 2',
    "command3": 'Command 3',
    "empty": 'iCQWEHGDCV',
    "command1func": 'iCQWEHGDCV',
    "command2func": 'iCQWEHGDCV',
    "command3func": 'iCQWEHGDCV',
    #---diagnostics
    "filescreatedtotal": 0,
    "filescreated": 0,
    "fileseditedtotal": 0,
    "filesedited": 0,
    "errorVariable": 0,
    "oneVariablePlaceHolder": 1,
    "errorVariableTotal": 0,
    "commandsExecuted": 0,
    "rawprint": 'iJRJHGEYBV',
    # add more variables here,
}
print('done "main"')

#---"codes" REFERENCE:---
#f: font code
#c: color code
#---"codes REFERENCE"---

codes = {
    #---color codes:
    "cPURPLE": '\033[95m',
    "cCYAN": '\033[96m',
    "cDARKCYAN": '\033[36m',
    "cBLUE": '\033[94m',
    "cGREEN": '\033[92m',
    "cYELLOW": '\033[93m',
    "cRED": '\033[91m',
    "cBOLD": '\033[1m',
    #---font codes
    "fUNDERLINE": '\033[4m',
    "fEND": '\033[0m',
    # add more variables here,
}
print('done "codes"')
