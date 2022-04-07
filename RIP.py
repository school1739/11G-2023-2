# import random
# # import random
# # class Player:
# #     def say(self, message):
# #         print(message)
# #     def sayShit(self):
# #         self.say("Пошёл ты!")
# #     def __init__(self, name):
# #         print ('Создан игрок')
# #         self.name = name
# #         self.age = random.randint(12,55)
# # class Player_inCapsule:
# #     def __init__(self, name, age):
# #         print("Создан инкапусированный игрок")
# #         self.__name=name
# #         self.__age=age
# #     def say_name(self):
# #         return self.__name
# #     def say_age(self):
# #         return  self.__age
# #
# #
# # Ivanov=Player("Inanoff")
# # Petrov=Player("Petroff")
# # # Ivanov.say("Дестиэль канон!")
# # # Petrov.sayShit()
# #
# # print(f"Player name: {Ivanov.name} Player age: {Ivanov.age}" )
# # print(f"Player name: {Petrov.name}     Player age: {Petrov.age}")
# # Ivanov.name="Was Ivanoff once"
# # Ivanov.age=78
# # Semenov=Player_inCapsule("Semion", 55)
# # # print(f"Player name: {Semenov.__name} Player age: {Semenov.__age}")
# # print(Semenov.say_age())
# # print(Semenov.say_name())
# class Dude:
#     def __init__(self, name):
#         self.__name= name
#         self.__age=random.randint(40,100)
#     def new_age(self, age):
#         if 0<age<100:
#             self.__age=age
#         else:
#             print("What?")
#     def show_AGE(self):
#         return self.__age
#     def show_ALL(self):
#         print(f"Name: {self.__name}, Age: {self.__age}")
#     def new_name(self, name):
#         self.__name=name
#     def show_name(self):
#         return self.__name
#
# class DudeJr(Dude):
#     def to_schoool(self, school):
#         print(f"{self.__name} is now at school number: #{school}")
#     def __init__(self, name):
#         self.__name= name
#         self.__age=random.randint(0,20)
#
# Rick= Dude("Rick")
# print(Rick.show_AGE())
# print(Rick.show_ALL())
# Rick.new_age(-45)
# Nick=DudeJr("Nick")
# Nick.to_schoool(1194)
# import random
# class Dude:
#     def __init__(self, name):
#         self.__name= name
#         self.__age=random.randint(40,100)
#
#     def get_name(self):  # функция-геттер
#         return self.__name
#
#     def set_name(self, name):# функция-сеттер
#         self.__name = name
#
#     def get_AGE(self):  # функция-геттер
#         return self.__age
#
#     def set_age(self, age): # функция-сеттер
#         if 0<age<100:
#             self.__age=age
#         else:
#             print("What?")
#
#     def get_info(self):
#         print(f"Name: {self.__name}, Age: {self.__age}")
# Rick=Dude("Rick")
# Rick.get_info()
# print(Rick.get_name())
# Rick.set_name("Nick")
# print(Rick.get_name())
import random

class Dude:
    def __init__(self, name):
        self.__name= name
        self.__age=random.randint(40,100)
    @property
    def name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name
    @property
    def AGE(self):
        return self.__age

    def set_age(self, age):
        if 0<age<100:
            self.__age=age
        else:
            print("What?")

    def get_info(self):
        print(f"Name: {self.__name}, Age: {self.__age}")