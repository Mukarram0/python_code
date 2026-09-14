device_status=input("enter status(active/offline): ").lower()

if(device_status=="active"):
    temp=int(input("enter temperature in celsius e.g: 25,30: "))
    if(temp>35):
        print("High Temperature")
    else:
        print("normal temperature ")
else:
    print("device is offline")