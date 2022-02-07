### Задание №5
##
#
import random

import simple_draw as sd


# функция для феерверка
def fireworks(point):
   for _ in range(25):
      radius = random.randint(3, 60)
      sd.circle(center_position=point, radius=radius, color=sd.random_color(), width=3)


# функция для полосок флага
def rectangle(left_bottom, right_top, color):
   sd.rectangle(left_bottom, right_top, color, width=0)


# функция для шарика
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
   start_point = sd.get_point(balloon_center[0], balloon_center[1] - 35)
   end_point = sd.get_point(balloon_center[0], balloon_center[1] - 75)
   sd.line(start_point, end_point, color=colour, width=1)


sd.background_color = (0, 0, 0)

# На заднем фоне нарисовать не менее трёх феерверков (группы разноцветных кругов разного
# относительно маленького диаметра, не менее 15 штук)
# феерверки
fireworks(sd.get_point(200, 550))
fireworks(sd.get_point(500, 300))
fireworks(sd.get_point(300, 100))
fireworks(sd.get_point(50, 300))

# Нарисовать флаг России с древком
# флаг
rectangle(sd.get_point(125, 425), sd.get_point(475, 500), (255, 255, 255))
rectangle(sd.get_point(125, 350), sd.get_point(475, 425), (0, 0, 250))
rectangle(sd.get_point(125, 275), sd.get_point(475, 350), (255, 0, 0))

# древко
rectangle(sd.get_point(115, 100), sd.get_point(125, 500), (127, 127, 0))

# Вокруг флага добавить не менее пяти воздушных шариков (эллипс + треугольник "хвостик" + прямая линия "ниточка")
balloon(balloon_center=[65, 525])
balloon(balloon_center=[515, 475])
balloon(balloon_center=[265, 245])
balloon(balloon_center=[75, 125])
balloon(balloon_center=[485, 155])
sd.pause()

# +-OK. Феерверки -- это области с несколькими маленькими пузыриками,
# а не концетрические круги.