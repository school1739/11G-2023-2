"""Представьте, что сумма за пользование услугами такси складывается из
базового тарифа в размере 4₽ плюс 0,25₽ за каждые 150 м поездки.
Напишите функцию, принимающую в качестве единственного параметра
расстояние поездки в километрах и возвращающую итоговую сумму опла-
ты такси. В основной программе должен демонстрироваться результат
вызова функции.

Может быть применен повышающий коэффициент. Используйте рандом для
подстановки коэффициента тарифа (от х1 -- обычный тариф до х2.5 -- повышенный."""
import random


def function(a):
    d = (4 + a / 3 * 5) * random.randint(10, 25) / 10
    return d


print("Введите длину поездки")
a = int(input())
print(function(a), "rub")
