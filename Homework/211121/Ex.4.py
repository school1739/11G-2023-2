### Задание 4. Приблизительное число π
##
# Делаем у пользьзователя звпрос
#
import math

print("Выбирите нужную Вам формулу, указав её порядковый номер.")
print("1. Формула Виета для приближения числа π")
print("2. Формула Валлиса")
print("3. Ряд Лейбница")
nomer_formuly = input("Введите номер: ")
print("До какого знака после запятой производить вычисления?")
kolichestvo_znakov = input("Введите количество знаков: ")
# Для формулы Виета
if nomer_formuly == "1":
    koren_iz_2 = math.sqrt(2)
    pi = 2 / koren_iz_2
    for i in range(int(kolichestvo_znakov) * 10):  # цикл для рачёта π
        koren_iz_2 = math.sqrt(2 + koren_iz_2)
        pi = 2 * pi / koren_iz_2
    final_pi_1 = round(2 * pi, int(kolichestvo_znakov))  # округление π до нужного количества занков
    print(final_pi_1)
# Для формулы Валлиса
elif nomer_formuly == "2":
    n = 1  # некая переменная
    pi = ((2 * n) ** 2) / ((2 * n - 1) * (2 * n + 1))
    for i in range(int(kolichestvo_znakov) * 10):  # цикл для расчёта π
        n += 1
        pi = pi * (2 * n) ** 2 / ((2 * n - 1) * (2 * n + 1))
    final_pi_2 = round(2 * pi, int(kolichestvo_znakov))  # округление π до нужного количества занков
    print(final_pi_2)
# Для ряда Лейбница
elif nomer_formuly == "3":
    k = 0  # некая переменная
    pi = (-1) ** k / (2 * k + 1)
    for i in range(int(kolichestvo_znakov) * 10):  # цикл для расчёта π
        k += 1
        pi = pi + ((-1) ** k) / (2 * k + 1)
    final_pi_3 = round(4 * pi, int(kolichestvo_znakov))  # округление π до нужного количества занков
    print(final_pi_3)
