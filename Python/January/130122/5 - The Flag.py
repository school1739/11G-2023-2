import simple_draw as sd


# Функция рисования флага России с древком
def flag(point):
    # Древко
    sd.line(
        sd.get_point(point.x - 150, point.y - 250),
        sd.get_point(point.x - 150, point.y + 100),
        (153, 77, 0),
        10
    )
    # Цикл для рисования полотна флага
    # с переменной w = шириной цветовой полоски
    w = 0
    for color in tricolor:
        sd.rectangle(
            sd.get_point(
                point.x - 150,
                point.y + 50 - w),
            sd.get_point(point.x + 150,
                         point.y + 100 - w),
            color
        )
        w += 50


# Функция Шарики
def balloon(point):
    # Сам шарик
    sd.ellipse(
        sd.get_point(point.x - 20, point.y - 30),
        sd.get_point(point.x + 20, point.y + 30),
        sd.random_color()
    )
    # Хвостик
    sd.polygon(
        point_list=(
            sd.get_point(point.x, point.y - 30),
            sd.get_point(point.x - 5, point.y - 40),
            sd.get_point(point.x + 5, point.y - 40)
        )
    )
    # Ниточка
    sd.line(
        sd.get_point(point.x, point.y - 40),
        sd.get_point(point.x, point.y - 100)
    )


# Функция Фейерверки
def fireworks():
    for i in range(4):
        sd.circle(
            sd.get_point(sd.random_number(100, 300) + i * 270,
                         sd.random_number(400, 800)
                         ),
            sd.random_number(1, 6),
            sd.random_color()
        )


# Задаём размер окна для вывода результата рисования
width = 1200
height = 600
sd.set_screen_size(width, height)
# Задаём параметр значений центра экрана
center = sd.get_point(width / 2, height / 2)

# Создаём список цветов для полосок флага
tricolor = [
    (255, 255, 255),
    (0, 0, 255),
    (255, 0, 0)
]

# На заднем фоне нарисовать не менее трёх фейерверков
# (группы разноцветных кругов разного
# относительно маленького диаметра, не менее 15 штук)
# Через цикл по функции fireworks() рисуем фейерверк
for i in range(100):
    fireworks()

# Вокруг флага добавить не менее пяти воздушных шариков
# (эллипс + треугольник "хвостик" + прямая линия "ниточка")
# Через цикл по функции balloon() рисуем воздушные шарики
for i in range(20):
    balloon(sd.random_point())

# Рисуем флаг через функцию flag() с точкой по центру экрана
flag(center)

sd.pause()

# OK