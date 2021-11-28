byte = str(input("Введите 8 бит "))
while byte != "":
    byte_count = byte.count("1")
    if len(byte) != 8: print("Ошибка")
    elif byte_count % 2 == 0: print("Бит четности = 1")
    elif byte_count % 2 != 0: print("Бит четности = 0")
    byte = str(input("Введите 8 бит "))