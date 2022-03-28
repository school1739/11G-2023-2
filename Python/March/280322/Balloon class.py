import simple_draw as sd
import random

"""
Задача: написать программу, выводящую на экран праздничный салют
и воздушные шарики, используя классы.
Салюты (5 салютов): 6 фейерверков (1 большой в центре, 5 в два раза
меньших вокруг). Фейерверк: не менее 15 закрашенных окружностей,
расположенных группой.
Шарик: основной овал, треугольник-пуцка, ломанная линия (не менее
4 отрезков) - верёвочка.
Фейерверки и шарики описываются в классах (обратите внимание на наследование!).
Постарайтесь максимально часто использовать рандом с небольшим разбросом,
чтобы не было одинаковых фигур.

Использование предопределенных классов обязательно. Дополнительные классы,
инкапсуляция, функции и классовые методы - произвольно.
Использование pygame и/или иных библиотек, кроме SD и random не допускается.
"""

class Firework: # Основной класс фейерверка
    def __init__(self):
        pass

class FireworkCenter(Firework): # Подкласс для большой центральной части фейерверка
    def draw_big(self):
        colors = ["red", "blue", "yellow"]
        center_pos = sd.ger_point(random.randint(0 , 500), random.randint(0, 500))
        self.center_pos = center_pos
        sd.circle(center_pos, radius=50, color=random.choice(colors), width=0)

big_circle = FireworkCenter()
big_circle.draw()
sd.pause

class FireworkAround(Firework): # Подкласс для маленьких фейерверков вокруг основного
    def draw_small(self):
        center_pos = sd.ger_point(random.randint(0, 500), random.randint(0, 500))
        self.center_pos = center_pos

class Balloon: # Класс для шарика
    pass