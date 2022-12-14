from commonFunctions import Common
import sqlite3
from time import sleep

class Forti: 
    def __init__(self): 
        self.master = "fortinet"
        self.wire = Common(self.master)

    def menuForti(self): 
        print("  Fortinet Menu  ".center(120,"$"))
        def innerFunc():
            ch = input("1-All devices in database\n2-Select and Show\n3-Send Script or Command\n4-Get Backup Config file\n5-Add devices into database\n(E/e) Exit----> ")
            if (ch == "E" or ch == "e"): 
                self.wire.shutDown()
            else: 
                if (ch == "1"): 
                    self.wire.getAllDevices()
                    innerFunc()

                elif (ch == "2"): 
                    quest = input("1-Select Device\n2-Show Selected Devices\n3-Select All Devices\n4-Remove From Selected\n5-Clear All Selected Devices\n(E/e) Exit----> ")
                    if (quest == "1"):
                        self.wire.selectDevices()
                        innerFunc()
                    elif (quest == "2"): 
                        self.wire.getSelectedDevices()
                        innerFunc()
                    elif (quest == "3"): 
                        self.wire.selectAllDevices()
                        innerFunc()
                    elif (quest == "4"): 
                        self.wire.removeFromSelected()
                        innerFunc()
                    elif (quest == "5"): 
                        self.wire.clearSelected()
                        innerFunc()
                    


                elif (ch == "3"): 
                    quest = input("1-Send Command\n2-Send Script\n\n----> ")
                    if (quest == "1"):
                        self.wire.sendCommand()
                        innerFunc()
                    elif (quest == "2"):
                        self.wire.sendScript()
                        innerFunc()

                elif (ch == "4"): 
                    p = input("1-Get full configuration from device manuelly\n2-Auto backup\n---> ")
                    if p == "1": 
                        self.wire.getConfig()
                    elif p == "2": 
                        self.wire.backupFunction("fortinet")
                    
                    innerFunc()
                
                elif (ch == "5"): 
                    connection = sqlite3.connect("devices.db")
                    cursor = connection.cursor()
                    sql_command = "INSERT INTO fortinet (name, ip) VALUES (?,?)"
                    devices = []
                    while True: 
                        device_name = input("Device Name: ")
                        ip = input("Ip address: ")
                        sure = input(f"device name:{device_name}, ip: {ip}\n----> Go and discard (g/d): ")
                        if (sure == "g" or sure == "G"): 
                            print("Ok..")
                            devices.append((device_name,ip))
                        else: 
                            print("Discarted. ")

                        stop = input("Do you want to continue to add device:(y/n): ")
                        if (stop == "y" or stop == "Y"): 
                            continue
                        elif (stop == "n" or stop == "N"): 
                            break
                        else: 
                            print("Out of index.")

                    for device in devices: 
                        try: 
                            cursor.execute(sql_command, device)
                            connection.commit()
                            print(f"This device {device} was added to database..")
                        except: 
                            print(f"This device {device} couldn't be added into database.")
                    innerFunc()

                else: 
                    print("Out of index. ")
                    innerFunc()


        innerFunc()