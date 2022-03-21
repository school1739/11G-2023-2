import random
class Player:
    def say(self, message):
        print(message)
    def sayShit(self):
        self.say("Пошёл ты!")
    def __init__(self, name):
        print ('Создан игрок')
        self.name = name
        self.age = random.randint(12,55)
class Player_inCapsule:
    def __init__(self, name, age):
        print("Создан инкапусированный игрок")
        self.__name=name
        self.__age=age
    def say_name(self):
        return self.__name
    def say_age(self):
        return  self.__age


Ivanov=Player("Inanoff")
Petrov=Player("Petroff")
# Ivanov.say("Дестиэль канон!")
# Petrov.sayShit()

print(f"Player name: {Ivanov.name} Player age: {Ivanov.age}" )
print(f"Player name: {Petrov.name}     Player age: {Petrov.age}")
Ivanov.name="Was Ivanoff once"
Ivanov.age=78
Semenov=Player_inCapsule("Semion", 55)
# print(f"Player name: {Semenov.__name} Player age: {Semenov.__age}")
print(Semenov.say_age())
print(Semenov.say_name())



