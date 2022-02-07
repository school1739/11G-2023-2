### Задание №1 "Bubbles"
import simple_draw as sd


# функция для пузырика
def puzyirik(point, step, colour):
   radius = 50
   for n in range(3):
      radius -= step
      sd.circle(center_position=point, radius=radius, color=colour, width=1)


# Нарисовать пузырек - три вложенных окружности с шагом 5 пикселей
point = sd.get_point(300, 550)
COLOR_WHITE = (255, 255, 255)
radius = 50
for n in range(3):
   radius -= 5
   sd.circle(center_position=point, radius=radius, color=COLOR_WHITE, width=1)

# Написать функцию рисования пузырька, принимающую 2 (или более) параметра: точка рисовании и шаг
# см. выше
# Нарисовать 10 пузырьков в ряд
for f in range(100, 1001, 100):
   point = sd.get_point(f, 450)
   puzyirik(point=point, step=5, colour=(255, 255, 255))

# Нарисовать три ряда по 10 пузырьков
for t in range(100, 301, 100):
   for f in range(100, 1001, 100):
      point = sd.get_point(f, t)
      puzyirik(point=point, step=5, colour=(255, 255, 255))

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for k in range(100):
   point = sd.random_point()
   colour = sd.random_color()
   puzyirik(point=point, step=5, colour=colour)
sd.pause()

# OK