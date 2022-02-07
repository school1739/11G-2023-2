"""Представьте, что сумма за пользование услугами такси складывается из
базового тарифа в размере 4₽ плюс 0,25₽ за каждые 150 м поездки.
Напишите функцию, принимающую в качестве единственного параметра
расстояние поездки в километрах и возвращающую итоговую сумму опла-
ты такси. В основной программе должен демонстрироваться результат
вызова функции.

Может быть применен повышающий коэффициент. Используйте рандом для
подстановки коэффициента тарифа (от х1 -- обычный тариф до х2.5 -- повышенный."""
import random #рандом
def taxi(km): #
    km = km * 1000 #метры
    cost = km // 150 #сколько раз проехали 150 метров
    r = random.uniform(1, 2.5) #рандомный кф
    print(r * ( 4 + (cost * 0.25))) #вывод стоимости:)
taxi(int(input("Введите км: ")))

# +-OK. Что за валюта такая? Бетховены?
# 47.25647971938261