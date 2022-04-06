import random

rounds = 0 #
def cheater(cheat, count_cheat):
    CHEAT = False

    if random.randint(5,100) <= cheat and count_cheat >= 3:
        CHEAT = True
    return CHEAT


count_1 = 0
count_2 = 0

fails_1 = 0
fails_2 = 0

class Player:
    def __init__(self, name):
        self.__name = name
        self.cheat = 0
        self.x=-1000
        self.y=1000
    def say_name(self):
        return self.__name
    def number(self, fails):
        if fails == 3:
            self.cheat += 5
        if cheater(self.cheat, fails) is True:
            self.x+=1000
            self.y+=1000
        self.num = random.randint(self.x, self.y)
        return self.num # вывод числа

player_1 = Player("Dean")
player_2 = Player("Sam")

class Judge:

    def Game(self):
        global fails_1, fails_2, count_1, count_2
        number_1 = player_1.number(fails_1)
        number_2 = player_2.number(fails_2)
        if number_1 == number_2:
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

        print( player_1.say_name() ," : ", count_1)
        print( player_2.say_name() ," : ", count_2)

judge = Judge()

while count_1 != 50 and count_2 != 50 and rounds != 100:
    judge.Game()
    rounds+=1
if count_1 == count_2:
    print("Ничью")
elif count_2 < count_1:
    print("Победил первый игрок")
else:
    print("Победил второй игрок")