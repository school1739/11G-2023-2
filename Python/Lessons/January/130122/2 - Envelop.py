# Заданы размеры envelop_x, envelop_y - размеры конверта и paper_x, paper_y листа бумаги
#
# Определить, поместится ли бумага в конверте (стороны листа параллельны сторонам конверта)
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

# TODO здесь ваш код

# Заданы размеры hole_x, hole_y прямоугольного отверстия и размеры brick_х, brick_у, brick_z кирпича (все размеры
# могут быть в диапазоне от 1 до 1000)
#
# Определить, пройдет ли кирпич через отверстие (грани кирпича параллельны сторонам отверстия)

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

# TODO здесь ваш код
#№1
k, q = int(input()), int(input())#конверт
b, p = int(input()), int(input())#бумага
if (k >= b and q >= p) or (k >= p and q >= b):
    print("ДА")
else:
    print("НЕТ")
l = [8,9,6,8,3,11,9]
n = [9,8,8,6,4,9,11]
for i in range(len(l)):
    if (k >= l[i] and q >= n[i]) or (k >= n[i] and q >= n[i]):
        print("ДА")
    else:
        print("НЕТ")
#№2
a,b = int(input()), int(input())
c,d,e= int(input()), int(input()),int(input())

if (a >= c and b >= d) or (a >= c and b >= e) or (a >= d and b >= c) or (a >= d and b >= e) or (a >= e and b >= c) or (a >= e and b >= d):
    print("ДА")
else:
    print("НЕТ")
l = [11,11,10,10,2,2,3,3,6,6,5,5,11,11,6,6,3,3]
m = [10, 2, 11, 2, 10, 11, 5, 6, 3, 5, 6, 3, 3, 6, 11, 3, 6, 11]
k = [2, 10, 2, 11, 11, 10, 6, 5, 5, 3, 3, 6, 6, 3, 3, 11, 11, 6]
for i in range(len(l)):
    if (a >= l[i] and b >= m[i]) or (a >= l[i] and b >= k[i]) or (a >= m[i] and b >= l[i]) or (a >= m[i] and b >= k[i]) or (a >= k[i] and b >= l[i]) or (a >= k[i] and b >= m[i]):
        print("ДА")
    else:
        print("НЕТ")

# NOT OK. Непонятно, что вводится, и зачем. И почему ввод не 2 чисел, а 4 и 5?