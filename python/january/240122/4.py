def center(s, w):
    sp = ""
    sps = " "
    if len(s) >= w:
        print(s)
    else:
        for i in range((w - len(s)) // 2):
            sp += sps
        print(sp + s)
center(input("Введите строку: "), int(input("Введите ширину окна: ")))