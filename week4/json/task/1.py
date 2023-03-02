import json
"""
with open("C:\KBTU\\2nd semester\pp2\TSIS4\json\sample-data.json") as f:
    data = json.loads(f.read())

"""
with open("C:\Users\77082\Desktop\python, tsis\week4\json\task\sample-data.json") as f:
    data= json.loads(f.read())

print("Interface Status")
print("============================================================================================================")
print("DN\t\t\t\t\t\tDescription\t\t\t\tSpeed\t\t\tMTU  ")
x=0
for i in data["imdata"]:
     print(data["imdata"][x]["l1PhysIf"]["attributes"]["dn"], end="\t\t\t")
     print(data["imdata"][x]["l1PhysIf"]["attributes"]["descr"], end="\t")
     print(data["imdata"][x]["l1PhysIf"]["attributes"]["speed"], end="\t\t\t")
     print(data["imdata"][x]["l1PhysIf"]["attributes"]["mtu"], end="\t")
     x+=1
