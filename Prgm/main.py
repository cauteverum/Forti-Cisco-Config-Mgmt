from os import system
from layerForti import Forti
from layerCisco import Cisco
import commonFunctions
import scheduledJob
import threading
from time import sleep

class Main: 
    def __init__(self): 
        self.flag = True
        self.menuThread = threading.Thread(target=self.mainMenu) 
        self.backupThread = threading.Thread(target=scheduledJob.this)
        self.menuThread.start()
        self.backupThread.start()
        

    def mainMenu(self): 
        system("color 0A")
        system("cls")
        while self.flag:
            print("  WELCOME  ".center(120,"$"))
            ch = input("1-Fortinet\n2-Cisco Switch or router\n3-Auto Backup\n(E/e) Exit\n----> ")
            if ch == "1": 
                fortiInstance = Forti()
                fortiInstance.menuForti()
            elif ch == '2': 
                ciscoInstance = Cisco()
                ciscoInstance.menuCisco()
            
            elif ch == '3': 
                t = input("1-Turn on auto backup\n2-Turn off auto backup\n---> ")
                if t == '1': 
                    scheduledJob.activated = True
                    print("Auto Backup Activated.")
                elif t == '2': 
                    scheduledJob.activated = False
                    print("Auto backup was closed.")
                else: 
                    print("Out of index.")

            elif (ch=='e' or ch=='E'): 
                self.flag = False
                scheduledJob.stop_thread = True
                scheduledJob.activated = False
                
                

Main()

