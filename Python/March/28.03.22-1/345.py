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
"""import random


class Dude:
    def __init__(self, name):
        self.__name = name
        self.__age = random.randint(40, 100)

    def new_age(self, age):
        if 0 < age < 100:
            self.__age = age
        else:
            print("WTF dude?")

    def show_age(self):
        return self.__age

    def new_name(self, name):
        self.__name=name

    def show_name(self):
        return self.__name

    def show_all(self):
        print(f"Name: {self.__name}, Age: {self.__age}")

class DudeJr(Dude):
    def __init__(self, name):
        self.__name = name
        self.__age = random.randint(0, 18)

    def to_school(self, school):
        print(f"{self.__name} is now at school #{school}")

Rick = Dude("Rick")
Rick.new_age(-45)
Rick.show_all()

Nick=DudeJr("Nick")
Nick.to_school(1194)"""
"""import random


class Dude:
    def __init__(self, name):
        self.__name = name
        self.__age = random.randint(40, 100)

    def get_name(self):  # Функция-геттер (GET)
        return self.__name

    def set_name(self, name):  # Функция-сеттер (SET)
        self.__name = name

    def get_age(self):  # Функция-геттер (GET)
        return self.__age

    def set_age(self, age):  # Функция-сеттер (SET)
        if 0 < age < 100:
            self.__age = age
        else:
            print("WTF dude?")

    def get_info(self):
        print(f"Name: {self.__name}, Age: {self.__age}")


rick = Dude("Rick")
rick.get_info()
print(rick.get_name())
rick.set_name("Nick")
print(rick.get_name())"""

import random


class Dude:
    def __init__(self, name):
        self.__name = name
        self.__age = random.randint(40, 100)

    @property
    def name(self):  # Функция-геттер (GET) с аннтоацией
        return self.__name

    @name.setter
    def name(self, name):  # Функция-сеттер (SET) с аннотацией
        self.__name = name

    @property
    def age(self):  # Функция-геттер (GET) с аннтоацией
        return self.__age

    @age.setter
    def age(self, age):  # Функция-сеттер (SET) с аннотацией
        if 0 < age < 100:
            self.__age = age
        else:
            print("WTF dude?")

    def get_info(self):
        print(f"Name: {self.__name}, Age: {self.__age}")


rick = Dude("Rick")
print(rick.name)
rick.name = "Nick"
print(rick.name)