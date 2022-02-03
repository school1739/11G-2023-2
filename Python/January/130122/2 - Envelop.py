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

envelop_t = int(input("Введите значение длины: "))
envelop_h = int(input("Введите значение ширины: "))
k = 0
# создаём цикл для проверки значений
for _ in range(7):
   if (znacheniya_1[k][0] < envelop_t and znacheniya_1[k][1] < envelop_h) or (
         znacheniya_1[k][0] < envelop_h and znacheniya_1[k][1] < envelop_t):
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
hole_t = int(input("Введите значение длины: "))
hole_h = int(input("Введите значение ширины: "))
i = 0
# создаём цикл для проверки
for _ in range(18):
   if (znacheniya_2[i][0] < hole_t and znacheniya_2[i][1] < hole_h) or (
         znacheniya_2[i][1] < hole_t and znacheniya_2[i][2] < hole_h) or (
         znacheniya_2[i][2] < hole_t and znacheniya_2[i][0] < hole_h):
      print('Да')
   else:
      print('Нет')
   i += 1
