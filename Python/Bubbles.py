import simple_draw as sd

# Нарисовать пузырек - три вложенных окружности с шагом 5 пикселей
point = sd.get_point(100,90)
radius=50
COLOR_BLUE = (0, 0, 255)
for i in range (3):
    radius+=5
    sd.circle(center_position=point, radius=radius, color=COLOR_BLUE, width=2)

# Написать функцию рисования пузырька, принимающую 2 (или более) параметра: точка рисовании и шаг
def circle(x,y, step):
    point = sd.get_point(x, y)
    radius = 10
    COLOR_GREEN = (0, 255, 0)
    for i in range(3):
        radius +=step
        sd.circle(center_position=point, radius=radius, color=COLOR_GREEN, width=2)

circle(50,50,5)
circle(200,200,10)


# Нарисовать 10 пузырьков в ряд

x=0
for i in range(10):
    x+=50
    circle(x, 500, 3)

# Нарисовать 100 пузырьков в произвольных   местах экрана случайными цветами
def Bubble(x,y,color):
    point1 = sd.get_point(x,y)
    radius = 10
    for i in range(3):
        radius += 3
        sd.circle(center_position=point1, radius=radius, color=color, width=2)
for i in range(101):

    x=sd.random_number()
    y=sd.random_number()
    Bubble(x, y, sd.random_color())

# Нарисовать три ряда по 10 пузырьков
x=0
for i in range(10):
    x+=50
    circle(x, 400, 3)
x = 0
for i in range(10):
    x += 50
    circle(x, 300, 3)
x=0
for i in range(10):
    x+=50
    circle(x, 200, 3)
sd.pause()