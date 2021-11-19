### Задание 5.
##
#
data_packet = input("Введите 8 бит (1 или 0): ")
if len(data_packet)==8:
    while data_packet != "":
        if data_packet.count("1")%2==0:
            print(data_packet+"1")
        else:
            print(data_packet+"0")
        data_packet=input("Введите 8 бит (1 или 0): ")
else:
    print("Нужно 8 знаков")
