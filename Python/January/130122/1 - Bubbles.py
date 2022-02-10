# Импортируем модуль библиотеки для рисования
import simple_draw as sd

# Задаём размер окна для вывода результата рисования
sd.set_screen_size(width=1200, height=600)
sd.start_drawing()


# Функция рисования пузырька,
# принимающая 2 (или более) параметра: точка рисовании и шаг
def draw_bubble(center, radius, step, color):
    for i in range(3):
        sd.circle(center, radius - i * step * 2, color)


# Функция рисования 10 пузырьков в ряд
def draw_bubble_row(y, radius, step, color):
    for i in range(10):
        draw_bubble(sd.get_point(radius * 2 * (i + 1), y), radius, step, color)


# Нарисовать пузырёк - три вложенных окружности с шагом 5 пикселей
draw_bubble(sd.Point(100, 500), 30, 5, sd.COLOR_PURPLE)

# Нарисовать 10 пузырьков в ряд
draw_bubble_row(200, 30, 5, sd.COLOR_CYAN)

# Нарисовать три ряда по 10 пузырьков
colors = [sd.COLOR_RED, sd.COLOR_BLUE, sd.COLOR_WHITE]
for i in range(3):
    draw_bubble_row(300 + i * 60, 30, 5, colors[i])

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for i in range(100):
    draw_bubble(sd.random_point(), 30, 5, sd.random_color())

sd.finish_drawing()
sd.pause()
