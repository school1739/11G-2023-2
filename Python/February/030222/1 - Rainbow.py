# (цикл for)

import simple_draw as sd

'''rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)'''

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# TODO здесь ваш код
# Подсказка: цикл нужно делать сразу по кортежу с цветами радуги.
def raduga ( step):
point = sd.start_point(50,50)
point1 = sd.end_point(350,450)
radius=10
step=5
rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
COLOR_RED = (255, 0, 0),
COLOR_ORANGE = (255, 127, 0),
COLOR_YELLOW = (255, 255, 0),
COLOR_GREEN = (0, 255, 0),
COLOR_CYAN = (0, 255, 255),
COLOR_BLUE = (0, 0, 255),
COLOR_PURPLE = (255, 0, 255)
for i in range (7):
    color+=color
    radius+=step
    sd.line(start_point=point, end_point=point1 , color=rainbow_colors, width=4,radius=radius):
    sd.pause()


# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
# TODO здесь ваш код

sd.pause()
