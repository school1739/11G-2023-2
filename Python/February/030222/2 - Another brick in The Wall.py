# (цикл for)
import simple_draw

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

# Задаём размер окна для вывода результата рисования
width = 1200
height = 600
simple_draw.set_screen_size(width, height)
# Задаём цвет шва в кирпичной кладке и рисуем им фон
simple_draw.rectangle(
    simple_draw.get_point(-width, -height),
    simple_draw.get_point(width, height),
    (100, 100, 100)
)

# Рисуем кирпичную стену
# Через цикл по оси y рисуем по два ряда кирпичей с размером шага для шва 10
for y in range(-height, height + 200, 120):
    # По оси x c шагом для шва размером 10
    for x in range(-width, width + 200, 110):
        # Сначала один ряд без сдвига одним цветом
        simple_draw.rectangle(
            simple_draw.get_point(x, y),
            simple_draw.get_point(x + 100, y + 50),
            (255, 118, 20)
        )
        # Следующий ряд другого цвета со сдвигом кирпичей по оси x на 50
        simple_draw.rectangle(
            simple_draw.get_point(x + 50, y + 60),
            simple_draw.get_point(x + 150, y + 110),
            (255, 133, 0)
        )

# Подсказки:
#  Для отрисовки кирпича использовать функцию rectangle
#  Алгоритм должен получиться приблизительно такой:
#
#   цикл по координате Y
#       вычисляем сдвиг ряда кирпичей
#       цикл координате X
#           вычисляем правый нижний и левый верхний углы кирпича
#           рисуем кирпич

simple_draw.pause()
