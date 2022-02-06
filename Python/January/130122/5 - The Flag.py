import simple_draw as sd

def flag():
    width = 0
    color_1 = (255, 243, 103)
    left_bottom_1 = sd.get_point(125, 425)
    right_top_1 = sd.get_point(425, 500)
    sd.rectangle(left_bottom_1, right_top_1, color=color_1, width=width)

    color_2 = (200, 200, 0)
    left_bottom_2 = sd.get_point(125, 350)
    right_top_2 = sd.get_point(425, 425)
    sd.rectangle(left_bottom_2, right_top_2, color=color_2, width=width)

    color_3 = (230, 255, 12)
    left_bottom_3 = sd.get_point(125, 275)
    right_top_3 = sd.get_point(425, 350)
    sd.rectangle(left_bottom_3, right_top_3, color=color_3, width=width)

    color_4 = (234, 133, 34)
    left_bottom_4 = sd.get_point(100, 100)
    right_top_4 = sd.get_point(125, 500)
    sd.rectangle(left_bottom_4, right_top_4, color=color_4, width=width)

def ferverk():
    radius_1 = 9
    radius_2 = 3
    radius_3 = 2
    radius_4 = 10
    width = 2
    center_pos_1 = sd.random_point()
    center_pos_2 = sd.random_point()
    center_pos_3 = sd.random_point()
    center_pos_4 = sd.random_point()
    for i in range(20):
        color_1 = sd.random_color()
        radius_1 += 4
        sd.circle(center_pos_1, radius=radius_1, color=color_1, width=width)
    for i in range(20):
        color_2 = sd.random_color()
        radius_2 += 4
        sd.circle(center_pos_2, radius=radius_2, color=color_2, width=width)
    for i in range(20):
        color_3 = sd.random_color()
        radius_3 += 6
        sd.circle(center_pos_3, radius=radius_3, color=color_3, width=width)
    for i in range(20):
        color_4 = sd.random_color()
        radius_4 += 5
        sd.circle(center_pos_4, radius=radius_4, color=color_4, width=width)




flag()
ferverk()
sd.pause()

# Нарисовать флаг России с древком

# Вокруг флага добавить не менее пяти воздушных шариков (эллипс + треугольник "хвостик" + прямая линия "ниточка")

# На заднем фоне нарисовать не менее трёх феерверков (группы разноцветных кругов разного
# относительно маленького диаметра, не менее 15 штук)

# Hint: для рисования однотипных объектов проще всего использовать функцию и цикл