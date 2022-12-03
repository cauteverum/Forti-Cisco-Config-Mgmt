import sqlite3
import schedule
import time
from netmiko import Netmiko
import datetime
import os 
activated = False
stop_thread = False

def this(): 
    def getDevices(): 
        sql_command = f"select * from backup"
        connection = sqlite3.connect("devices.db")
        cursor = connection.cursor()
        cursor.execute(sql_command)
        devices = cursor.fetchall()
        return devices

    def path(): 
        user = os.getcwd().split("\\")[2]
        if not os.path.exists(f"C:/users/{user}/desktop/backupfordevices/fortinet"): 
            os.makedirs(f"C:/users/{user}/desktop/backupfordevices/fortinet")
        if not os.path.exists(f"C:/users/{user}/desktop/backupfordevices/cisco"): 
            os.makedirs(f"C:/users/{user}/desktop/backupfordevices/cisco")

    def doJob(devices=list): 
        user = os.getcwd().split("\\")[2]
        for device in devices: 
            try: 
                if device[3] == "fortinet":
                    dct = {
                        "host":device[2], 
                        "username":"admin", 
                        "password":"admin",
                        "device_type":device[3]
                    }
                    connect = Netmiko(**dct)
                    # print(f"connected to {device[1]}")
                    res = connect.send_command("show full-configuration")

                    foldername = datetime.datetime.now().strftime("%Y-%m-%d")
                    if not os.path.exists(f"C:/users/{user}/desktop/backupfordevices/{dct['device_type']}/{foldername}"): 
                        os.makedirs(f"C:/users/{user}/desktop/backupfordevices/fortinet/{foldername}")

                    with open(file=f"C:/users/{user}/desktop/backupfordevices/fortinet/{foldername}/{device[1] + '_' + datetime.datetime.now().strftime('%Y-%m-%d--%H-%M')}.cfg", mode="w",encoding="utf-8") as file: 
                        file.write(res)

                        
                elif device[3] == "cisco": 
                    dct = {
                        "ip":device[2], 
                        "username":"onur", 
                        "password":"onur",
                        "secret":"onur",
                        "device_type":device[3] + "_ios"
                    }
                    connect = Netmiko(**dct)
                    # print(f"connected to {device[1]}")
                    res = connect.send_command("show run")
                    foldername = datetime.datetime.now().strftime("%Y-%m-%d")

                    if not os.path.exists(f"C:/users/{user}/desktop/backupfordevices/cisco/{foldername}"): 
                        os.makedirs(f"C:/users/{user}/desktop/backupfordevices/cisco/{foldername}")

                    with open(file=f"C:/users/{user}/desktop/backupfordevices/cisco/{foldername}/{device[1] + '_' + datetime.datetime.now().strftime('%Y-%m-%d--%H-%M')}.cfg", mode="w",encoding="utf-8") as file: 
                        file.write(res)

            except: 
                print(f"Occured an issues as connecting this device: {device[1]}")


    
    schedule.every(12).hours.do(this)
    while True: 
        time.sleep(1)
        if activated: 
            devices = getDevices()
            path()
            doJob(devices=devices)
            schedule.run_pending()
            time.sleep(2)
        if stop_thread: 
            break

