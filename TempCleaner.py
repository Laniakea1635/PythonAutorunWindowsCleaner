import os
from winreg import *
from os import path
import time
import getpass

PathFile = path.abspath(__file__)

def Startup():
    StartupKey = OpenKey(HKEY_CURRENT_USER,
                    r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run',
                    0, KEY_ALL_ACCESS)
    SetValueEx(StartupKey, 'name', 0, REG_SZ, PathFile)
    CloseKey(StartupKey)

Startup()


deleteFiles = ["C:/Users/"+getpass.getuser()+"/AppData/Local/Temp","C:/Windows/Temp","C:/Windows/LiveKernelReports","C:/Windows/Offline Web Pages","C:/Windows/Offline Web Pages","C:/Windows/Downloaded Program Files"]
for directory in deleteFiles:
    print("Directory: " + directory)
    for f in os.listdir(directory):
        try:
            print("Deleted: " + f)
            os.remove(os.path.join(directory, f))
        except:
            print("Can't delete: " + f)
            continue
