### Задание №1 "Rainbow"
##
#
import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)

for i in range(7):
    start = [50, 50]
    end = [350, 450]
    start_point = sd.get_point(start[0] - (i * 5), start[1])
    end_point = sd.get_point(end[0] - (i * 5), end[1])
    sd.line(start_point, end_point, color=rainbow_colors[i], width=4)

# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана

point = sd.get_point(300, 0)
radius = 200
for i in range(7):
    radius -= 10
    sd.circle(point, radius, color=rainbow_colors[i], width=10)
sd.pause()
