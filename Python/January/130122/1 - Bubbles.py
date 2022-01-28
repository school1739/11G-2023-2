import simple_draw as sd

# Нарисовать пузырек - три вложенных окружности с шагом 5 пикселей

point = sd.get_point(100, 100)
radius = 50
for i in range(3):
    radius += 5
    sd.circle(center_position=point, radius=radius, color=(255, 0, 255), width=2)


# Написать функцию рисования пузырька, принимающую 2 (или более) параметра: точка рисовании и шаг
def bubbles(point, step):
    radius = 50
    colour = sd.random_color()
    for i in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, color=colour, width=2)


# Нарисовать 10 пузырьков в ряд
for x in range(100, 1001, 100):
    point = sd.get_point(x, 450)
    bubbles(point=point, step=5)

# Нарисовать три ряда по 10 пузырьков
for y in range(100, 301, 100):
    for x in range(100, 1001, 100):
        point = sd.get_point(x, y)
        bubbles(point=point, step=5)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for p in range(100):
    point = sd.random_point()
    bubbles(point=point, step=10)

sd.pause()
