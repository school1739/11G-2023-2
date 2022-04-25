# инкапсуляция
# форматированный выво
# лигатуры
# работа с классами при повторяющихся объеутами!

import random


def globalSay(msg):
    print(msg)


class Player:
    def __init__(self, name, age):
        print("Создан инкапсулированный игрок")
        self.__name = name
        self.__age = random.randint(12, 55)

    def say(self, message):
        print(message)

    def sayShit(self):
        self.say("Shit!")

    def sayGlobal(self):
        globalSay("Shit global")


Ivanov = Player("Ivanoff")
Petrov = Player("P.E. Trove")

print(f"player name: {Ivanov.name}      PLayer age: {Ivanov.age}")
