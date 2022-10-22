lang = input("Выберите язык RU/EU: ")

alf_EU = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
alf_RU = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

if lang == 'EU':
    choice = int(input("1 - шифрование, 2 - дешифровка, 3 - перебор брутом: "))

    def chifr(sdvig): # Шифровка
        global alf_EU
        stroka_for_shifr = input("Вы выбрали режим шифрование, введите строку для шифрования: ").upper()
        itog_shifr = ""
        for i in stroka_for_shifr:
            ind = alf_EU.find(i)
            new_ind = ind + sdvig
            if i in alf_EU: itog_shifr += alf_EU[new_ind]

            else: itog_shifr += i
        return itog_shifr


    def deshifr(isv_sdvig):  # Дешифровка
        global alf_EU
        stroka_for_deshifr = input("Вы выбрали режим дешифрование, введите строку для дешифрования: ").upper()
        itog_deshifr = ""
        for i in stroka_for_deshifr:
            ind = alf_EU.find(i)
            new_ind = ind - isv_sdvig
            if i in alf_EU:
                itog_deshifr += alf_EU[new_ind]
            else:
                itog_deshifr += i
        return itog_deshifr


    def brut():  # Брут
        global alf_EU
        stroka_for_shifr = input("Вы выбрали режим брут, введите строку для дешифрования: ").upper()
        for sdvig in range(1, 26):
            itog_shifr = ""
            for i in stroka_for_shifr:
                mesto = alf_EU.find(i)
                new_mesto = mesto + sdvig
                if i in alf_EU:
                    itog_shifr += alf_EU[new_mesto]
                else:
                    itog_shifr += i
            print("При sdvig == " + str(sdvig) + " шифровщик выдает - " + str(itog_shifr))


    if choice == 1:
        sdvig = int(input("Введите сдвиг: "))
        print(chifr(sdvig))

    if choice == 2:
        isv_sdvig = int(input("Введите сдвиг, который использовался при шифровании строки: "))
        print(deshifr(isv_sdvig))

    if choice == 3:
        brut()

else:
    choice = int(input("1 - шифрование, 2 - дешифровка, 3 - перебор брутом: "))

    def chifr(sdvig):  # Шифровка
        global alf_RU
        stroka_for_shifr = input("Вы выбрали режим шифрование, введите строку для шифрования: ").upper()
        itog_shifr = ""
        for i in stroka_for_shifr:
            ind = alf_RU.find(i)
            new_ind = ind + sdvig
            if i in alf_RU:
                itog_shifr += alf_RU[new_ind]

            else:
                itog_shifr += i
        return itog_shifr

    def deshifr(isv_sdvig): #Дешифровка
        global alf_RU
        stroka_for_deshifr = input("Вы выбрали режим дешифрование, введите строку для дешифрования: ").upper()
        itog_deshifr = ""
        for i in stroka_for_deshifr:
            ind = alf_RU.find(i)
            new_ind = ind - isv_sdvig
            if i in alf_RU: itog_deshifr += alf_RU[new_ind]
            else:itog_deshifr += i
        return itog_deshifr

    def brut(): # Брут
        global alf_RU
        stroka_for_shifr = input("Вы выбрали режим брут, введите строку для дешифрования: ").upper()
        for sdvig in range(1, 26):
            itog_shifr = ""
            for i in stroka_for_shifr:
                mesto = alf_RU.find(i)
                new_mesto = mesto + sdvig
                if i in alf_RU:
                    itog_shifr += alf_RU[new_mesto]
                else:
                    itog_shifr += i
            print("При sdvig == " + str(sdvig) + " шифровщик выдает - " + str(itog_shifr))

    if choice == 1:
        sdvig = int(input("Введите сдвиг: "))
        print(chifr(sdvig))

    if choice == 2:
        isv_sdvig = int(input("Введите сдвиг, который использовался при шифровании строки: "))
        print(deshifr(isv_sdvig))

    if choice == 3:
        brut()