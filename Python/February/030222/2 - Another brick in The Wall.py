# (цикл for)
import simple_draw as sd

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
sd.set_screen_size(500,500)
point=[0,50]
for i in range(10):
    left_bottom=sd.get_point(point[0]-35, point[1]-15)
    right_top=sd.get_point(point[0]+35, point[1]+15)
    sd.rectangle(left_bottom,right_top, color=(127,127,0), width=0)
    point[0]+=70

sd.pause()
