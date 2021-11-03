#Grach_Fe

import random

print("Это игра в рулетку")
user_number - int(input("Введите своё число"))
user_color = str(input("Введите цвет (карсное, черное или зеленое) "))
user_chet_nechet = str(input("Введите четное или нечетное число "))
user_diapazon = str(input("Введите диапазон числа (от 0 - 18(цифра 1) / от 19 - 36(цифра 2)) "))
#Grach_Fe
red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
green = [0, 00]
all = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36, 0, 00]

chet = [0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36]
nechet = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35]
#Grach_Fe
diapazon_1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
diapazon_2 = [19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]

mac_number = random.choice(all)

print("Выпавшее число: " + str(mac_number))
if user_number == comp_number:
    print("Выигрышная ставка:" + str(mac_number))  #Grach_Fe

if mac_number in red and user_color == "красное":
    print("Выигрышная ставка: красное")
if mac_number in black and user_color == "черное":
    print("Выигрышная ставка: черное")
if mac_number in green and user_color == "зеленое":
    print("Выигрышная ставка: зеленое")

if mac_number in chet and user_chet_nechet == "четное":
    print("Выигрышная ставка: четная")
if mac_number in nechet and user_chet_nechet == "нечетное":
    print("Выигрышная ставка: нечетная")

if mac_number in diapazon_1 and user_diapazon == 1:
    print("Выигрышная ставка: от 1 до 18")
if mac_number in diapazon_2 and user_diapazon == 2:
    print("Выигрышная ставка от 19 до 36")
#Grach_Fe