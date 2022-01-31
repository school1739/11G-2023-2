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

summa_numbers_player_1 = 0
summa_numbers_player_2 = 0


def player_1():
    chislo_player_1 = random.randint(0, 1000)
    return chislo_player_1


def player_2():
    chislo_player_2 = random.randint(0, 1000)
    return chislo_player_2


def sudia():
    global summa_numbers_player_1
    global summa_numbers_player_2
    for i in range(100):
        player_2()
        player_1()
        if player_1() == player_2():
            summa_numbers_player_1 += 1
            summa_numbers_player_2 += 1
        elif player_1() > player_2():
            summa_numbers_player_1 += 1
            summa_numbers_player_2 -= 1
        elif player_2() > player_1():
            summa_numbers_player_1 -= 1
            summa_numbers_player_2 += 1
        if summa_numbers_player_1 >= 50:
            print("WINNER is player 1 ")
        if summa_numbers_player_2 >= 50:
            print("WINNER is 2 player")

    print(summa_numbers_player_2, summa_numbers_player_1)

#хрень с рандомом, не хвататет только его, определяется всего лишь 1 раз на все иттерации цикла
#вызывать функцию возврата в цикле
sudia()

