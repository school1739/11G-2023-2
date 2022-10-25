choice = int(input("1 - шифрование, 2 - дешифровка, 3 - перебрать брутом --> "))
l = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"

def chifr(sdvig): #Функция для шифровки
    global l
    stroka_for_shifr = input("Вы выбрали режим шифрование, введите строку для шифрования(only english, а то русскую лень делать, та и по заданию уточнений не было:)) --> ").upper()
    itog_shifr = ""
    for i in stroka_for_shifr:
        ind = l.find(i)
        new_ind = ind + sdvig
        if i in l: itog_shifr += l[new_ind]

        else: itog_shifr += i
    return itog_shifr

def deshifr(isv_sdvig): #Функция для дешифровки
    global l
    stroka_for_deshifr = input("Вы выбрали режим дешифрование, введите строку  для дешифрования(only english, а то русскую лень делать, та и по заданию уточнений не было:)) --> ").upper()
    itog_deshifr = ""
    for i in stroka_for_deshifr:
        ind = l.find(i)
        new_ind = ind - isv_sdvig
        if i in l: itog_deshifr += l[new_ind]
        else:itog_deshifr += i
    return itog_deshifr



def brut(): #Функция для брута
    global l
    stroka_for_shifr = input("Вы выбрали режим брут, введите строку для дешифрования(only english, а то русскую лень делать, та и по заданию уточнений не было:))--> ").upper()
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
    isv_sdvig = int(input("Введите сдвиг, который использовался при шифровании строки --> "))
    print(deshifr(isv_sdvig))

if choice == 3:
    brut()
