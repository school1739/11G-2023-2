data_packet = input()
if len(data_packet)==8:
    while data_packet != "":
        if data_packet.count("1")%2==0:
            print(data_packet+"1")
        else:
            print(data_packet+"0")
        data_packet=input()
else:
    print("Нужно 8 знаков")
