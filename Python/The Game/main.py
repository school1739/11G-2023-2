"""Написать программу, где две функции -- "Игрок 1" и "Игрок 2"
играют в игру, а третья функция -- "Судья" -- следит за ходом игры
и ведёт счёт.

Правила игры:
Оба игрока кажый раунд выдают случайное целое число
в некотором диапазоне. Судья сравнивает эти числа и начисляет игрокам очки:
Если числа равны, оба игрока получают 1 очко (+1). Когда число одно из игроков
больше другого, игрок, который выдал большее число, получает 1 очко (+1),
другой игрок штрафуется на 1 очко (-1). Игра продолжается до тех пор, пока
один из игроков не наберёт 50 очков, но не более 100 раундов."""


"""UPDATE 1:
Режим "Читера": после 3 проигрышей увеличивается вероятность "чита".
Чит: увеличение randint range на (+1000, +1000).
Изначальная вероятность считерить: 0%. Увеличение вероятности: +5%.
После первой победы с читом чит отключается. Вероятность чита сохраняется."""

import random

summa_numbers_player_1 = 0
summa_numbers_player_2 = 0
numbers_1 = []
numbers_2 = []
p1_1 = -1000
p1_2 = 1000
p2_1 = -1000
p2_2 = 1000

def player_1():
    chislo_player_1 = random.randint(p1_1, p1_2)
    return chislo_player_1


def player_2():
    chislo_player_2 = random.randint(p2_1, p2_2)
    return chislo_player_2

for i in range(100):     #создание списков выпавших чисел для обоих игроков
    numbers_1.append(player_1())
    numbers_2.append(player_2())
print(numbers_1)
print(numbers_2)

def cheat_mode():  #чит мод
    global p1_1
    global p1_2
    global p2_1
    global p2_2

    global summa_numbers_player_1
    global summa_numbers_player_2

    ver = 1.05
    f_pl1 = 0
    f_pl2 = 0

    if summa_numbers_player_1 - summa_numbers_player_2 >= 3:
        p2_1 += 1000
        p2_2 += 1000

    if summa_numbers_player_2 - summa_numbers_player_1 >= 3:
        p1_1 += 1000
        p1_2 += 1000


def sudia():
    global summa_numbers_player_1
    global summa_numbers_player_2


    for i in range(100):
        a = numbers_1[i]
        b = numbers_2[i]
        if a == b:
            summa_numbers_player_1 += 1
            summa_numbers_player_2 += 1
        elif a > b:
            summa_numbers_player_1 += 1
            summa_numbers_player_2 -= 1
        elif a < b:
            summa_numbers_player_1 -= 1
            summa_numbers_player_2 += 1
        elif summa_numbers_player_1 >= 50:
            print("WINNER is player 1 ")
            break
        elif summa_numbers_player_2 >= 50:
            print("WINNER is 2 player")
            break
        print(summa_numbers_player_1, summa_numbers_player_2)
        print()

        if summa_numbers_player_2 - summa_numbers_player_1 == 3 or summa_numbers_player_1 - summa_numbers_player_2 == 3:
            cheat_mode()


sudia()

#какая-то дичь с рандомом
#попробовать 100 раз вызвать функции player_1 и player_2, значения запихать в 2 списка, а уже потом в дургом цикле
#проходится по каждому элементу первого и второго списка и сравнивать их значения и прибавлять баллы по условию
