### Задание №2 "Envelop"
##
#
# значения бумаги, данные для сравнения
znacheniya_1 = [
   [8, 9],
   [9, 8],
   [6, 8],
   [8, 6],
   [3, 4],
   [11, 9],
   [9, 11],
]

# Запрашиваем у пользователя значенеия

envelop_x = int(input("Введите значение длины: "))
envelop_y = int(input("Введите значение ширины: "))
k = 0
# создаём цикл для проверки значений
for _ in range(7):
   if (znacheniya_1[k][0] < envelop_x and znacheniya_1[k][1] < envelop_y) or (
         znacheniya_1[k][0] < envelop_y and znacheniya_1[k][1] < envelop_x):
      print('Да')
   else:
      print('Нет')
   k += 1
# все значения кирпича, данные для сравнения
znacheniya_2 = [

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
# запрашиваем значения у пользователя
hole_x = int(input("Введите значение длины: "))
hole_y = int(input("Введите значение ширины: "))
i = 0
# создаём цикл для проверки
for _ in range(18):
   if (znacheniya_2[i][0] < hole_x and znacheniya_2[i][1] < hole_y) or (
         znacheniya_2[i][1] < hole_x and znacheniya_2[i][2] < hole_y) or (
         znacheniya_2[i][2] < hole_x and znacheniya_2[i][0] < hole_y):
      print('Да')
   else:
      print('Нет')
   i += 1

# OK. Накосячил с отступами