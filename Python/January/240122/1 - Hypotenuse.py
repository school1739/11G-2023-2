### Задание №1 "Hypotenuse"
##
#
# функция для расчёта гипотенузы
def hypo(k1, k2):
   hypotenuse = (k1 ** 2 + k2 ** 2) ** 0.5
   print("Гипотенуза равна", hypotenuse)


# запрашиваем у пользователя значения катетов
katet_1 = int(input("Введите значение первого катета: "))
katet_2 = int(input("Введите значение второго катета: "))

# вызов функции
hypo(katet_1, katet_2)
