import random

rounds=0 # счётчик раундов
def cheater(cheat, count_cheat): # функция читерства
    CHEAT = False # будет работать чит или нет
# условие для работы чита
    if random.randint(5,100) <= cheat and count_cheat >= 3:
        CHEAT = True
    return CHEAT

# Счётчики очков
count_1 = 0
count_2 = 0
# счётчики проигрышей
fails_1 = 0
fails_2 = 0

class Player: # класс игрока
    def __init__(self, name):
        self.__name = name
        self.cheat = 0
        self.x=-1000 # циферки для рандома
        self.y=1000
    def say_name(self): # getter
        return self.__name
    def number(self, fails): # Функция вызова числа
        if fails == 3:
            self.cheat += 5
        if cheater(self.cheat, fails) is True: # работа чита
            self.x+=1000
            self.y+=1000
        self.num = random.randint(self.x, self.y)
        return self.num # вывод числа

player_1 = Player("Dean")
player_2 = Player("Sam")

class Judge:
    def __init__(self):
        print("GO!")
    def Game(self): # работа судьи
        global fails_1
        global fails_2
        global count_1
        global count_2
        number_1 = player_1.number(fails_1) # числа игроков, в зависимости от кол-ва проигрышей
        number_2 = player_2.number(fails_2)
        if number_1 == number_2: # проверяем условия начисления очков
            count_1 += 1
            count_2 += 1
            fails_1+=0
            fails_2+=0
        elif number_1 > number_2:
            count_1 += 1
            count_2 -= 1
            fails_2 += 1
        else:
            count_1 -= 1
            count_2 += 1
            fails_1 += 1
        # вывод очков
        print( player_1.say_name() ,": ", count_1) # выводим кол-во очков
        print( player_2.say_name() ,": ", count_2)

judge = Judge()
# сама игра с учётом продолжительности
while count_1 != 50 and count_2 != 50 and rounds != 100:
    judge.Game()
    rounds+=1
if count_1 == count_2: # выводим, кто победил
    print("Победила дружба")
elif count_2 < count_1:
    print("Победил первый игрок")
else:
    print("Победил второй игрок")