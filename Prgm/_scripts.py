import pandas as pd 
from netmiko import Netmiko
# import pandas as pd 
# import sqlite3
# connection = sqlite3.connect("devices.db")
# cursor = connection.cursor()

df = pd.read_excel("envanter.xlsx")[["NAME","IP"]]
# print(df)


df = df[["NAME","IP"]]
df = df[(df["IP"].notnull() & df["IP"].str.contains("http"))]
names, ips, zip_ = [], [], ()
for name in df["NAME"]: 
    names.append(name)
for ip in df["IP"]:
    s = ip.split("https://")[1].split(":")[0]
    ips.append(ip)


sql_command = "INSERT INTO fortinet (name, ip) VALUES (?,?)"
zip_ = list(zip(names,ips))
for i in range (len(zip_)):
    try:
        cursor.execute(sql_command,zip_[i])
        connection.commit()
        print(f"This pair was added to database: {zip_[i]}")
    except:
        print(f"This ip {zip_[i][1]} address exist in database: ")
