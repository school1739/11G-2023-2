"""import random


def globalSay(msg):
    print(msg)


class Player_inCapsule:
    def __init__(self, name, age):
        print("Создан инкапуслированный игрок")
        self.__name = name
        self.__age = age

    def say_name(self):
        return self.__name

    def say_age(self):
        return self.__age


class Player:
    def __init__(self, name):
        print("Конструктор создал игрока")
        self.name = name
        self.age = random.randint(12, 55)

    def say(self, message):
        print(message)

    def sayShit(self):
        self.say("Shit!")

    def sayGlobal(self):
        globalSay("Shit global")


Ivanov = Player("Ivanoff")
Petrov = Player("P.E. Trove")

print(f"Player name: {Ivanov.name}      Player age: {Ivanov.age}")
print(f"Player name: {Petrov.name}      Player age: {Petrov.age}")

Ivanov.name = "Was Ivanoff once"
Ivanov.age = 78

print()
print(f"Player name: {Ivanov.name}      Player age: {Ivanov.age}")

print()
Semenoff = Player_inCapsule("SemiOne", 55)

print(Semenoff.say_age())
print(Semenoff.say_name())
"""

class Dude:
    def __init__(self, name):
        self.__name = name
        self.__ade = random.randint(0, 100)

    def new_age(self, age):
        self.__age = age


    def show_age(self):
        return self.__age
    def show_all(self):
    print(f"Name: {self.__name}, Age: {self.__age}")
Rick = Dude("Rick")
print(Rick.__age)