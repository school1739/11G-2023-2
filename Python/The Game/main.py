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

import random

p1_number = 0
p2_number = 0


def p1():
    global p1_number
    p1_number = random.randint(-1000, 1000)
    return p1_number


def p2():
    global p2_number
    p2_number = random.randint(-1000, 1000)
    return p2_number


def judge():
    global p1_number
    global p2_number
    count_1 = 0
    count_2 = 0
    rounds = 0
    while rounds <=100 or count_1 <= 50 or count_2 <= 50:
        if p1_number == p2_number:
            count_1 += 1
            count_2 += 1
        elif p1_number > p2_number:
            count_1 += 1
            count_2 -= 1
        else:
            count_1 -= 1
            count_2 += 1
        print("Первый игрок: ", count_1)
        print("Второй игрок: ", count_2)
        rounds += 1
    if count_1 == count_2:
        print("Победила дружба")
    elif count_2 < count_1:
        print("Победил первый игрок")
    else:
        print("Победил второй игрок")


p1()
p2()
judge()
