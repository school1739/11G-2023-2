### Balloons and Fireworks classes
##
#
import simple_draw as sd
import random

class Firework: # Основной класс фейерверка
    def __init__(self, point):
        self.color=sd.random_color()
        self.point=point

class FireworkCenter(Firework): # Подкласс для большой центральной части фейерверка
    def FC(self):
        for _ in range(15):
            radius = 6
            sd.circle(center_position=sd.get_point(self.point[0]-random.randint(-50,50), self.point[1]-random.randint(-50,50)), radius=radius, color=self.color, width=0)

class FireworkAround(FireworkCenter): # Подкласс для маленьких фейерверков вокруг основного
    def FA(self):
        for _ in range(5):
            for _ in range(15):
                radius=3
                sd.circle(center_position=sd.get_point(self.point[0]-random.randint(-100, 100), self.point[1]-random.randint(-100, 100)), radius=radius, color=self.color, width=0)

class Balloon: # Класс для шарика
    def balloon(balloon_center):
        # сам шарик
        color = sd.random_color()
        left_bottom = sd.get_point(balloon_center[0] - 15, balloon_center[1] - 25)
        right_top = sd.get_point(balloon_center[0] + 15, balloon_center[1] + 25)
        sd.ellipse(left_bottom, right_top, color=color, width=0)
        # пуцка
        sd.polygon(point_list=[sd.get_point(balloon_center[0], balloon_center[1] - 25),
                               sd.get_point(balloon_center[0] - 3, balloon_center[1] - 35),
                               sd.get_point(balloon_center[0] + 3, balloon_center[1] - 35)],
                   color=color, width=0)
        # верёвочка
        colour = sd.random_color()
        sd.lines(point_list=[sd.get_point(balloon_center[0], balloon_center[1] - 35),
                             sd.get_point(balloon_center[0], balloon_center[1] - 45),
                             sd.get_point(balloon_center[0] + 5, balloon_center[1] - 60),
                             sd.get_point(balloon_center[0] - 2, balloon_center[1] - 75),
                             sd.get_point(balloon_center[0], balloon_center[1] - 90)],
                 color=colour, width=1)

sd.background_color = (0, 0, 0)
# шарики
b_1 = Balloon
for _ in range(15):
    b_1.balloon((random.randint(0, 600), random.randint(0, 600)))
# салюты
fa_1 = FireworkAround((300, 300))
fa_1.FA()
f_1=FireworkCenter((300,300))
f_1.FC()

fa_2 = FireworkAround((125, 475))
fa_2.FA()
f_2=FireworkCenter((125,475))
f_2.FC()

fa_3 = FireworkAround((125, 125))
fa_3.FA()
f_3=FireworkCenter((125,125))
f_3.FC()


fa_4 = FireworkAround((475, 475))
fa_4.FA()
f_4=FireworkCenter((475,475))
f_4.FC()

fa_5 = FireworkAround((475, 125))
fa_5.FA()
f_5=FireworkCenter((475,125))
f_5.FC()
#  ещё шарики
for _ in range(10):
    b_1.balloon((random.randint(0, 600), random.randint(0, 600)))

sd.pause()