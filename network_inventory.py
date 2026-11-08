devices=[ ]
devices.append({"name":"jays_law", "ip": "192.168.10.1", "type":"switch",})
print (devices)
ip= ('USER IP')
types= ("device_type")
while True:
    menu =input ('1, Add device\n 2, View Device\n 3, Search Device\n 4,Exit\n')
    print (menu)
    if menu ==("1"):
        print("welcom")
        for i in range (1):
            devices_name= input("enter a name to add a new device\n")
            ip= input("enter ip address for the device \n")
            types= input("choose device type\n")
            devices.append({"name": devices_name, "ip": ip, "type": types})
            
    elif menu ==("2"):
        print (devices)   

    elif menu ==("3"):

        search_name= input  (" enter a name to search for a device ")
        found= False
        for device in devices:
            if device["name"]== search_name:
                print (device)
                found=True
        if found== False:
            print("no device found")
    elif menu ==("4"):
        exit()   

