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
    def __init__(self):
        pass

class FireworkCenter(Firework): # Подкласс для большой центральной части фейерверка
    pass
    def draw_1(self):
        #colors =  ['red' 'blue' 'yellow']
        center_pos = sd.get_point(random.randint(0, 500), random.randint(0, 500))
        self.center_pos = center_pos
        COLOR_WHITE = (255, 255, 255)
        sd.circle(center_position=center_pos, radius=60, color=COLOR_WHITE, width=0)
fare = FireworkCenter()
fare.draw_1()
class FireworkAround(Firework): # Подкласс для маленьких фейерверков вокруг основного
    def s(self):
        COLOR_ORANGE = (255, 127, 0)
        center_pos = sd.get_point(random.randint(300, 500), random.randint(300, 500))
        for i in range(5):
            center_pos = sd.get_point(random.randint(300, 500), random.randint(300, 500))
            sd.circle(center_position=center_pos, radius=60, color=COLOR_ORANGE, width=0)
s = FireworkAround()
s.s()
class Balloon: # Класс для шарика
    pass
sd.pause()