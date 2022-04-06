import simple_draw as sd
import random

"""
Задача: написать программу, выводящую на экран праздничный салют
и воздушные шарики, используя классы.
Салют: 5 групп по 6 фейерверков (1 большой в центре, 5 в два раза
меньших вокруг). Фейерверк: не менее 15 закрашенных окружностей,
расположенных группой.
Шарик: основной овал, треугольник-пуцка, ломанная линия (не менее
4 отрезков) - верёвочка.
Фейерверки и шарики описываются в классах (обратите внимание на наследование!).
Постарайтесь максимально часто использовать рандом с небольшим разбросом,
чтобы не было одинаковых фигур.

Использование предопределенных классов обязательно. Дополнительные классы,
инкапсуляция, функции и классовые методы -- произвольно.
Использование pygame и/или иных библиотек, кроме SD и random не допускается.
"""

class Firework: # Основной класс фейерверка
    pass

class FireworkCenter(Firework): # Подкласс для большой центральной части фейерверка
    pass
    def draw_1(self):
        COLOR_WHITE = (255, 255, 255)
        COLOR_RED = (255, 0, 0)
        COLOR_YELLOW = (255, 255, 0)
        COLOR_DARK_YELLOW = (127, 127, 0)
        COLOR_DARK_ORANGE = (127, 63, 0)
        colors_1 = [COLOR_RED, COLOR_DARK_ORANGE, COLOR_YELLOW, COLOR_DARK_YELLOW, COLOR_WHITE]
        for i in range(15):
            center_pos = sd.get_point(random.randint(200, 400), random.randint(200, 400))
            sd.circle(center_position=center_pos, radius=24, color=random.choice(colors_1), width=0)


class FireworkAround(Firework): # Подкласс для маленьких фейерверков вокруг основного
    def draw_2(self):
        COLOR_ORANGE = (255, 127, 0)
        COLOR_GREEN = (0, 255, 0)
        COLOR_CYAN = (0, 255, 255)
        COLOR_BLUE = (0, 0, 255)
        COLOR_PURPLE = (255, 0, 255)
        colors_2 = [COLOR_BLUE, COLOR_PURPLE, COLOR_ORANGE, COLOR_GREEN, COLOR_CYAN]
        for q in range(5):
            for i in range(15):
                center_pos = sd.get_point(random.randint(100, 700), random.randint(100, 700))
                sd.circle(center_position=center_pos, radius=12, color=random.choice(colors_2), width=0)



class Balloon: # Класс для шарика
    def draw_3(balloon_center):

        COLOR_ORANGE = (255, 127, 0)
        COLOR_GREEN = (0, 255, 0)
        COLOR_CYAN = (0, 255, 255)
        COLOR_BLUE = (0, 0, 255)
        COLOR_PURPLE = (255, 0, 255)
        colors_2 = [COLOR_BLUE, COLOR_PURPLE, COLOR_ORANGE, COLOR_GREEN, COLOR_CYAN]
        left_bottom = sd.get_point(balloon_center[0] - 15, balloon_center[1] - 25)
        right_top = sd.get_point(balloon_center[0] + 15, balloon_center[1] + 25)
        sd.ellipse(left_bottom, right_top, color=random.choice(colors_2), width=0)

        sd.polygon(point_list=[sd.get_point(balloon_center[0], balloon_center[1] - 25),
                               sd.get_point(balloon_center[0] - 3, balloon_center[1] - 35),
                               sd.get_point(balloon_center[0] + 3, balloon_center[1] - 35)],
                   color=random.choice(colors_2), width=0)


        sd.lines(point_list=[sd.get_point(balloon_center[0], balloon_center[1] - 35),
                             sd.get_point(balloon_center[0], balloon_center[1] - 45),
                             sd.get_point(balloon_center[0] + 5, balloon_center[1] - 60),
                             sd.get_point(balloon_center[0] - 2, balloon_center[1] - 75),
                             sd.get_point(balloon_center[0], balloon_center[1] - 90)],
                 color=random.choice(colors_2), width=1)

sd.background_color = (0, 0, 0)


fare = FireworkCenter()
fare.draw_1()

draw_2 = FireworkAround()
draw_2.draw_2()

bal = Balloon
for i in range(15):
    bal.draw_3((random.randint(0, 600), random.randint(0, 600)))

sd.pause()