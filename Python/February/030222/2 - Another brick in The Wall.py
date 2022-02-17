# (цикл for)

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

# TODO здесь ваш код
# Подсказки:
#  Для отрисовки кирпича использовать функцию rectangle
#  Алгоритм должен получиться приблизительно такой:
#
#   цикл по координате Y
#       вычисляем сдвиг ряда кирпичей
#       цикл координате X
#           вычисляем правый нижний и левый верхний углы кирпича
#           рисуем кирпич
import simple_draw as sd

a = (100, 50)
b = (100,) * 3
c = 10
d = 10
f = 10

sd.rectangle(sd.get_point(0, 0), sd.get_point(*sd.resolution), b)
for i in range(f):
    for j in range(d):
        x = (a[0] + c) * i
        y = (a[1] + c) * j
        if y % 2 == 1:
            x -= (a[0] + c) / 2
        start = sd.get_point(x, y)
        end = sd.get_point(x + a[0], y + a[1])
        sd.rectangle(start, end, sd.COLOR_ORANGE)
sd.pause()
