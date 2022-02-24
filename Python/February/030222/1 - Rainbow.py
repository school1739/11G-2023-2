# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# Задаём размер окна для вывода результата рисования
width = 1200
height = 600
sd.set_screen_size(width, height)
# Задаём начальную и конечную точку полос радуги по оси х
x1 = 50
x2 = 350
# Задаём цикл по кортежу с цветами радуги
for i in rainbow_colors:
    sd.line(
        start_point=sd.get_point(x1, 50),
        end_point=sd.get_point(x2, 450),
        color=i,
        width=4
    )
    # Добавляем шаг по оси x
    x1 += 5
    x2 += 5
# Подсказка: цикл нужно делать сразу по кортежу с цветами радуги.


# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
# Задаём переменную для радиуса окружностей
r = 400
# Задаём цикл по кортежу с цветами радуги
for i in rainbow_colors:
    sd.circle(
        center_position=sd.get_point(650, -100),
        radius=r,
        color=i,
        width=20
    )
    # Шаг сдвига радиуса
    r += 20

sd.pause()
