# Заданы размеры envelop_x, envelop_y - размеры конверта
# и paper_x, paper_y листа бумаги
#
# Определить, поместится ли бумага в конверте
# (стороны листа параллельны сторонам конверта)
#
# Результат проверки вывести на консоль (ДА/НЕТ)
# Использовать только операторы if/elif/else, можно вложенные

# АВТОМАТИЧЕСКИ проверить для:
# paper_x, paper_y = 8, 9
# paper_x, paper_y = 9, 8
# paper_x, paper_y = 6, 8
# paper_x, paper_y = 8, 6
# paper_x, paper_y = 3, 4
# paper_x, paper_y = 11, 9
# paper_x, paper_y = 9, 11
# (написать цикл для проверки)
# script_name Wughy

# Ипмортируем функцию permutations()
# для разных комбинации перестановки элементов списка, включая смену порядка
from itertools import permutations

# Запрашиваем у пользователя размеры конверта
envelop_x = float(input("Введите значение длины конверта: "))
envelop_y = float(input("Введите значение ширины конверта: "))

# Размеры листов бумаги
sizes_papers = [(8, 9), (9, 8), (6, 8), (8, 6), (3, 4), (11, 9), (9, 11)]

# Задаём цикл по всем размерам листов бумаги,
# чтобы проверить поместится ли бумага в конверте.
# Учитывается, что лист д.б. немного меньше конверта (из-за толщины бумаги),
# т.е. размеры не должны быть равны.
for size in sizes_papers:
    if size[0] < envelop_x and size[1] < envelop_y or \
       size[0] < envelop_y and size[1] < envelop_x:
        print("ДА")
    else:
        print("НЕТ")

# Заданы размеры hole_x, hole_y прямоугольного отверстия
# и размеры brick_х, brick_у, brick_z кирпича
# (все размеры могут быть в диапазоне от 1 до 1000)
#
# Определить, пройдет ли кирпич через отверстие
# (грани кирпича параллельны сторонам отверстия)

# АВТОМАТИЧЕСКИ проверить для:
# brick_x, brick_y, brick_z = 11, 10, 2
# brick_x, brick_y, brick_z = 11, 2, 10
# brick_x, brick_y, brick_z = 10, 11, 2
# brick_x, brick_y, brick_z = 10, 2, 11
# brick_x, brick_y, brick_z = 2, 10, 11
# brick_x, brick_y, brick_z = 2, 11, 10
# brick_x, brick_y, brick_z = 3, 5, 6
# brick_x, brick_y, brick_z = 3, 6, 5
# brick_x, brick_y, brick_z = 6, 3, 5
# brick_x, brick_y, brick_z = 6, 5, 3
# brick_x, brick_y, brick_z = 5, 6, 3
# brick_x, brick_y, brick_z = 5, 3, 6
# brick_x, brick_y, brick_z = 11, 3, 6
# brick_x, brick_y, brick_z = 11, 6, 3
# brick_x, brick_y, brick_z = 6, 11, 3
# brick_x, brick_y, brick_z = 6, 3, 11
# brick_x, brick_y, brick_z = 3, 6, 11
# brick_x, brick_y, brick_z = 3, 11, 6
# (написать цикл для проверки)

# Запрашиваем значения размеров отверстия у пользователя
hole_x = float(input("Введите значение длины отверстия: "))
hole_y = float(input("Введите значение ширины отверстия: "))

# Размеры кирпичей
sizes_bricks = [
    (11, 10, 2), (11, 2, 10), (10, 11, 2), (10, 2, 11), (2, 10, 11),
    (2, 11, 10), (3, 5, 6), (3, 6, 5), (6, 3, 5), (6, 5, 3), (5, 6, 3),
    (5, 3, 6), (11, 3, 6), (11, 6, 3), (6, 11, 3), (6, 3, 11),
    (3, 6, 11), (3, 11, 6)
]

# Задаём цикл по всем размерам кирпичей
for size in sizes_bricks:
    # Проверяем, пройдет ли кирпич через отверстие хотя бы одной гранью кирпича
    if any(face[0] <= hole_x and face[1] <= hole_y
           for face in permutations(size, 2)):
        print("ДА")
    else:
        print("НЕТ")

# OK