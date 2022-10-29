# from netmiko import Netmiko
# from getpass import getpass
import pandas as pd 

# # ls = []
# # stps = []
# # for i in range(1,999): 
# #     t = i
# #     stp = 1
# #     while True: 
# #         if (t == 1): 
# #             res = f"{i} is Collatz number . Step: {stp}"
# #             print(res)
# #             ls.append(res)
# #             stps.append(stp)
# #             break

# #         elif (t%2==0): 
# #             t = t/2

# #         elif (t%2 != 0): 
# #             t = t*3 + 1
# #         stp += 1

# # for i in ls: 
# #     if not "Collatz" in i:
# #         print("Found exception...") 
# # print(max(stps))


# # ls = test.split("\n")
# # newString = ""
# # for i in ls: 
# #     control = i.strip()
# #     if control == "set utm-status enable": 
# #         ls[ls.index(i)] = "        set utm-status disable"

# # for i in ls: 
# #     newString = newString + i + "\n"

# # print(newString)



# dst_1 = "10.10.100.0/24"
# gateway_1 = "192.168.0.1"
# device_1 = "port1"
# comment_1 ="Comment_one"

# dst_2 = "10.10.90.0/24"
# gateway_2 = "192.168.0.1"
# device_2 = "port1"
# comment_2 ="Comment_two"


# dst_3 = "10.10.110.0/24"
# gateway_3 = "192.168.0.1"
# device_3 = "port1"
# comment_3 ="Comment_three"

# ls = [(dst_1,gateway_1,device_1,comment_1),(dst_2,gateway_2,device_2,comment_2)]
# script = "config router static\n"
# for i in ls: 
#     if i == ls[-1]: 
#         tx = f"edit 0\nset dst {i[0]}\nset gateway {i[1]}\nset device {i[2]}\nset comment {i[3]}\nend\n"
#         script = script + tx
#     else: 
#         tx = f"edit 0\nset dst {i[0]}\nset gateway {i[1]}\nset device {i[2]}\nset comment {i[3]}\nnext\n"
#         script = script + tx

# with open(file="scp.txt",mode="w",encoding="utf-8") as file: 
#     file.write(script)


# pswd = getpass("password: ")
# dct = {
#     "host":"192.168.0.128",
#     "username": "admin",
#     "password":pswd,
#     "device_type":"fortinet"
# }
# connection = Netmiko(**dct)
# res=connection.send_config_from_file("scp.txt")
# print(res)
