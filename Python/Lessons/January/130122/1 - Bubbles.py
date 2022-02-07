import simple_draw as sd
import random
center_pos_ex = sd.get_point(300, 300)
COLOR_white = (255, 255, 255)     #ознакомление с библиотекой
sd.circle(center_pos_ex, radius=10, color=COLOR_white, width=1)


# Нарисовать пузырек - три вложенных окружности с шагом 5 пикселей
shag = 5
radius = 40
color = (255, 255, 0)
center_pos = sd.get_point(200, 200)
for i in range(3):
    sd.circle(center_pos, radius=radius, color=color, width=3)
    radius += shag

# Написать функцию рисования пузырька, принимающую 2 (или более) параметра: точка рисовании и шаг
def puz(center_pos, color, shag):
    radius = 40
    for i in range(3):
        radius -= shag
        sd.circle(center_position=center_pos, radius=radius, color=color, width=2)
center_pos = sd.get_point(50,400)
puz(center_pos, (255,0,0), 5)
# Нарисовать 10 пузырьков в ряд
x = 30
for i in range(10):
    center_pos = sd.get_point(x, 100)
    puz(center_pos, (255,0,0), 10)
    x += 60

# Нарисовать три ряда по 10 пузырьков
for y2 in range(300, 401, 50):
    for x2 in range(50, 550, 50):
        center_pos = sd.get_point(x2, y2)
        puz(center_pos, (255, 255, 0), 5)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for i in range(100):
    x3 = random.randint(0, 600)
    y3 = random.randint(0, 600)
    center_pos = sd.get_point(x3, y3)
    color = sd.random_color()
    puz(center_pos, color, 5)
sd.pause()

# OK. Наведи порядок в репозитории! Пришлось искать, где лежат задания.