choice = int(input("1 - шифрование, 2 - дешифровка, 3 - перебрать брутом -->"))
l = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def chifr(sdvig): #дешифровка и брут в процессе
    global l
    stroka_for_shifr = input("Вы выбрали режим шифрование, введите строку для шифрования --> ").upper()
    itog_shifr = ""
    for i in stroka_for_shifr:
        mesto = l.find(i)
        new_mesto = mesto + sdvig
        if i in l:
            itog_shifr += l[new_mesto]
        else: itog_shifr += i
    return itog_shifr
def deshifr():
    pass
def brut():
    global l
    print("Вы выбрали режим брут")
    stroka_for_shifr = input("Вы выбрали режим шифрование, введите строку для шифрования --> ").upper()
    for sdvig in range(1, 26):

        itog_shifr = ""
        for i in stroka_for_shifr:
            mesto = l.find(i)
            new_mesto = mesto + sdvig
            if i in l:
                itog_shifr += l[new_mesto]
            else:
                itog_shifr += i
        print("При sdvig == " + str(sdvig) + " шифровщик выдает - " + str(itog_shifr))

if choice == 1:
    sdvig = int(input("Введите сдвиг --> "))
    print(chifr(sdvig))

if choice == 2:
    deshifr()
if choice == 3:
    brut()
