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

from random import randint

max_rounds = 10000
max_points = 50


# class player
class Player:
    # constructor
    def __init__(self):
        self.points = 0
        self.range = [-1000, 1000]
        self.defeats_in_row = 0
        self.cheat_chance = 0

    # make_turn
    def make_turn(self):
        self.try_cheat()
        return randint(*self.range)

    # cheat after 3 loses
    def try_cheat(self):
        if self.defeats_in_row >= 3:
            self.defeats_in_row = 0
            self.cheat_chance += 5
            if self.cheat_chance > 95:
                self.cheat_chance = 95
            if randint(0, 100) <= self.cheat_chance:
                self.range[0] += 1000
                self.range[1] += 1000

    # win
    def win(self):
        self.defeats_in_row = 0

    # draw
    def draw(self):
        self.win()

    # lose
    def lose(self):
        self.defeats_in_row += 1


# class judge
class Judge:
    # Конструктор класса
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    # play_round
    def iteration(self):
        choice1 = self.player1.make_turn()
        choice2 = self.player2.make_turn()
        if choice1 == choice2:
            self.player1.draw()
            self.player2.draw()
            self.add_points(1, 1)
        elif choice1 > choice2:
            self.player1.win()
            self.player2.lose()
            self.add_points(1, -1)
        else:
            self.player1.lose()
            self.player2.win()
            self.add_points(-1, 1)

        if self.player1.points >= max_points and self.player2.points >= max_points:
            return 'Ничья!'
        if self.player1.points >= max_points:
            return '1-ый игрок выиграл!'
        if self.player2.points >= max_points:
            return '2-ой игрок выиграл!'
        return None

    # rounds_over
    def rounds_over(self):
        if self.player1.points == max_points and self.player2.points >= max_points:
            return 'Ничья!'
        if self.player1.points > self.player2.points:
            return '1-ый игрок выиграл!'
        return '2-ой игрок выиграл!'

    # add_points
    def add_points(self, p1, p2):
        self.player1.points += p1
        self.player2.points += p2


# player and judge
player1 = Player()
player2 = Player()
judge = Judge(player1, player2)

# cycle
for i in range(max_rounds):
    result = judge.iteration()

    print(f'Ход {i + 1}. Очки: {(player1.points, player2.points)}. Ranges: {(player1.range, player2.range)}')

    if result is not None:
        print(result)
        break
# rounds are over
else:
    print('Раунды кончились!')
    print(judge.rounds_over())