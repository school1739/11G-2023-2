### Задание №2
##
# Есть значение радиуса круга
#
radius = 42
pi = 3.1415926
# Вычислим площадь круга
print(round((pi * (radius ** 2)), 4))
# Есть координаты двух точек
sites = {'Point_1': (23, 34),
         'Point_2': (30, 30),
         }
point_1 = sites["Point_1"]
point_2 = sites["Point_2"]
# Если точка лежит внутри того самого круга [центр в начале координат (0, 0), radius = 42],
# то выведем на консоль True, Или False, если точка лежит вовне круга.
# Аналогично для другой точки
distance_1 = (point_1[0] ** 2 + point_1[1] ** 2) ** 0.5
distance_2 = (point_2[0] ** 2 + point_2[1] ** 2) ** 0.5
if distance_1 <= radius:
    print("True")
else:
    print("False")
if distance_2 <= radius:
    print("True")
else:
    print("False")
