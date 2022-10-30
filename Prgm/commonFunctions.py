import sqlite3
from pandas import DataFrame
from netmiko import Netmiko
from getpass import getpass

class Common: 
    def __init__(self,whoisMaster): 
        self.selected = []
        self.connection = sqlite3.connect("devices.db")
        self.cursor = self.connection.cursor()
        self.master = whoisMaster

    def getSelectedDevices(self): 
        if len(self.selected) > 0: 
            info = self.convertToDf(self.selected)
            print(f"$$$$$$$$$$       DEVICES YOU SELECTED       $$$$$$$$$$\n{info}")
        else: 
            print("Warning----> You didn't select any device yet. ")

    def shutDown(self): 
        print(f"{self.master} connection is being closed...")
        self.connection.close()

    def convertToDf(self,devices=list): 
        id, name, ip = [], [], []
        dct = {
            'id' : id,
            'name': name, 
            'ip' : ip
        }
        for device in devices: 
            id.append(device[0])
            name.append(device[1])
            ip.append(device[2])

        df = DataFrame(dct)
        blankIndex=['-->'] * len(df)
        df.index=blankIndex
        if len(df) == 0: 
            print("You've not selected any device yet.\n")
        elif len(df) != 0: 
            return df

    def getAllDevices(self):
        self.cursor.execute(f"select * from {self.master}")
        devices = self.cursor.fetchall()
        res = self.convertToDf(devices)
        print(f"{res} ")

    def clearSelected(self): 
        self.selected.clear()
        print("Removed all devices from selected devices.")


    def selectAllDevices(self): 
        self.cursor.execute(f"select * from {self.master}")
        devices = self.cursor.fetchall()
        self.selected.clear()
        self.selected = devices
        print("Selected all devices.")

    def selectDevices(self):
            deviceIDs = ""
            try:
                question_ = input("1-I want to see devices before selecting. \n2-Select device: \n-----> ")
                if question_ == "1": 
                    self.getAllDevices()
                    deviceIDs = input("Device Ids in format (a,b,c,d): ")
                elif question_ == "2": 
                    deviceIDs = input("Device Ids in format (a,b,c,d): ")

                sql = f"select * from {self.master} where id=?"   
                device_IDs = deviceIDs.split(',')
                for id in device_IDs: 
                    self.cursor.execute(sql,[id])
                    res = self.cursor.fetchone()
                    if res in self.selected: 
                        print("This element already exist in selected devices.")
                    else:
                        self.selected.append(res)

                result = self.convertToDf(self.selected)
                print(f"The devices you selected: \n{result}")
            except: 
                print(f"Syntax Error or index doesn't exist.")


    def removeFromSelected(self): 
        ids = input("Type ID of devices that you want to delete. This format should be like  (id1,id2,id3): ").split(",")
        for id in ids: 
            found_ = False
            for element in self.selected: 
                if element[0] == int(id):         
                    index = self.selected.index(element)
                    self.selected.pop(index)
                    print(f"The device that has id {id} was removed from selected devices. ")
                    found_ = True
            if not found_: 
                print(f"This id({id}) doesn't exist in selected devices.")



    def getConfig(self): 
        myList = []
        command_  = ""
        uname = input("Username: ")
        psw = input("Password: ")
        dname = ""
        print(self.selected)
        for device  in self.selected: 
            host= device[2]
            dct = {
                'host' : host, 
                'username': uname,
                'password': psw, 
                'device_type': self.master
            }
            myList.append(dct)
        i=0
        for device in myList: 
            if self.master == "fortinet": 
                command_ = "show full-configuration"
            elif self.master == "cisco": 
                command_ = "show running config"
            try:
                nm = str(self.selected[i][1]) + ".txt"
                dname = str(self.selected[i][1])
                with open(file=nm, mode='w',encoding='utf-8') as file: 
                    deviceConnection = Netmiko(**device)
                    full_config = deviceConnection.send_command(command_)
                    file.writelines(full_config)
                    print(f"'{self.selected[i][1]}' backup file has been saved.")
                i += 1
            except Exception: 
                print(f"Error: {dname}.")


    def sendCommand(self): 
        myList = []
        uname = input("Username: ")
        psw = input("Password: ")     
        for device in self.selected: 
            host = device[2]
            dct = {
                'host' : host, 
                'username' : uname,
                'password' : psw, 
                'device_type' : 'fortinet'
            }
            myList.append(dct)
        try: 
            for device in myList: 
                device_connection = Netmiko(**device)
                print("Type q or quit To disconnect current device")
                while True: 
                    cmd = input("Command: ") 
                    if (cmd == "q" or cmd == "quit"): 
                        break
                    output = device_connection.send_command(cmd)
                    print(f"Command info:\n{output}")
        except Exception: 
            print("Error.")

    def sendScript(self): 
        myList = []
        uname = input("Username: ")
        psw = input("Password: ")
        sricpt_path = input("Script path: ")
        for device in self.selected: 
            host = device[2]
            dct = {
                'host' : host, 
                'username' : uname,
                'password' : psw, 
                'device_type' : 'fortinet'
            }
            myList.append(dct)
        print(myList)
        try:
            for device in myList: 
                deviceConnection = Netmiko(**device)
                output = deviceConnection.send_config_from_file(sricpt_path)
                print(f"Command info:\n {output}")
        except Exception: 
            print("Error.")
