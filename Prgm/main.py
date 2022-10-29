from os import system
from layerForti import Forti
from layerCisco import Cisco
import commonFunctions


class Main: 
    def __init__(self): 
        self.flag = True
    
    def mainMenu(self): 
        system("color 0A")
        system("cls")
        while self.flag:
            print("  WELCOME  ".center(120,"$"))
            ch = input("1-Fortinet\n2-Cisco Switch or router\n(E/e) Exit\n----> ")
            if ch == "1": 
                fortiInstance = Forti()
                fortiInstance.menuForti()
            elif ch == '2': 
                ciscoInstance = Cisco()
                ciscoInstance.menuCisco()

            elif (ch=='e' or ch=='E'): 
                self.flag = False

instance_main = Main()
instance_main.mainMenu()