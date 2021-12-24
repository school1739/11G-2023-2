import math


# функция для расчета расстояния
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


# первая координата
first_point = (float(input("x =")), float(input("y =")))
last_point = first_point
perimeter = 0

# сюда пусть вставляет числа чел
while True:
    x = input("x=")

    if x == '':
        perimeter += distance(last_point, first_point)
        break

    y = input("y=")

    new_point = (float(x), float(y))
    perimeter += distance(new_point, last_point)
    last_point = new_point

print("Perimeter = {0:.2f}".format(perimeter))

# Evaluation: OK