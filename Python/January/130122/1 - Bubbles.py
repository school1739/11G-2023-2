import simple_draw as sd

# Нарисовать пузырек - три вложенных окружности с шагом 5 пикселей
def a(point, step, colour):
    c = 50
    for i in range(3):
        radius -= step
        sd.circle(center_position=point, radius=radius, color=colour, width=1)
# Написать функцию рисования пузырька, принимающую 2 (или более) параметра: точка рисовании и шаг
a = sd.get_point(300, 550)
b = (255, 255, 255)
for i in range(3):
    radius -= 5
    sd.circle(center_position=a, radius=c, color=b, width=1)
# Нарисовать 10 пузырьков в ряд
def a(point, step, colour):
for i in range(100, 1000, 100):
    b = sd.get_point(i, 450)
    a(point=b, step=5, colour=(255, 255, 255))
# Нарисовать три ряда по 10 пузырьков
for i in range(100, 300, 100):
    for j in range(100, 1000, 100):
        b = sd.get_point(j, i)
        a(point=b, step=5, colour=(255, 255, 255))
# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for i in range(100):
    b = sd.random_point()
    c = sd.random_color()
    a(point=point, step=5, colour=colour)
sd.pause()