# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
start_x = 50
start_y = 50
end_x = 350
end_y = 450
for i in range(7):
    start_x += 5
    end_x += +5
    sd.line(start_point=sd.get_point(start_x, start_y), end_point=sd.get_point(end_x, end_y), color=rainbow_colors[i],
            width=4)

# Подсказка: цикл нужно делать сразу по кортежу с цветами радуги.


# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
import time

point = sd.get_point(600, -500)
radius = 900
q = 0
for radius in range(900, 600, -10):
    time.sleep(0.3)
    sd.circle(center_position=point, radius=radius, color=rainbow_colors[q], width=10)
    q += 1
    if q == 7:
        break
sd.pause()
