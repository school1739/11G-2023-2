1 = [
    [8, 9],
    [9, 8],
    [6, 8],
    [8, 6],
    [3, 4],
    [11, 9],
    [9, 11],
]

envelop_x = int(input("Введите значение длины: "))
envelop_y = int(input("Введите значение ширины: "))
k = 0

for _ in range(7):
    if (1[k][0] < envelop_x and 1[k][1] < envelop_y) or (
            1[k][0] < envelop_y and 1[k][1] < envelop_x):
        print('Да')
    else:
        print('Нет')
    k += 1

2 = [

    [11, 10, 2],
    [11, 2, 10],
    [10, 11, 2],
    [10, 2, 11],
    [2, 10, 11],
    [2, 11, 10],
    [3, 5, 6],
    [3, 6, 5],
    [6, 3, 5],
    [6, 5, 3],
    [5, 6, 3],
    [5, 3, 6],
    [11, 3, 6],
    [11, 6, 3],
    [6, 11, 3],
    [6, 3, 11],
    [3, 6, 11],
    [3, 11, 6],

]

hole_x = int(input("Введите значение длины: "))
hole_y = int(input("Введите значение ширины: "))
i = 0

for _ in range(18):
    if (znacheniya_2[i][0] < hole_x and znacheniya_2[i][1] < hole_y) or (
            2[i][1] < hole_x and 2[i][2] < hole_y) or (
            2[i][2] < hole_x and 2[i][0] < hole_y):
        print('Да')
    else:
        print('Нет')
    i += 1