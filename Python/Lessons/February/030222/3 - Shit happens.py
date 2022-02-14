# (определение функций)
import simple_draw as sd

# Написать функцию отрисовки смайлика по заданным координатам
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Под смайликом сделать подпись "Shit happens"

# TODO здесь ваш код
def big_circle():
    color = (255, 242, 0)
    radius = 150
    start_point_smile = sd.get_point(300, 400)
    width = 0
    sd.circle(center_position=start_point_smile, radius=radius, color=color, width=width)
def two_small_eyes():
    color = (0, 0, 0)
    radius = 40
    start_point1 = sd.get_point(250, 450)
    start_point2 = sd.get_point(350, 450)
    width = 0
    sd.circle(start_point1, color=color, radius=radius, width=width)
    sd.circle(start_point2, color=color, width=width, radius=radius)
def two_very_small_eyes():
    color = (255, 255, 255)
    radius = 20
    start_point1 = sd.get_point(250, 450)
    start_point2 = sd.get_point(350, 450)
    width = 0
    sd.circle(start_point1, color=color, radius=radius, width=width)
    sd.circle(start_point2, color=color, width=width, radius=radius)
def ylibka():
    color = (0, 0, 0)
    width = 6
    point_list = [sd.get_point(220, 320), sd.get_point(250, 300), sd.get_point(350, 300), sd.get_point(380, 320)]
    sd.lines(point_list, color=color, closed=False, width=width)



def shit(): #эх... ну понеслась...
    pass

big_circle()
two_small_eyes()
two_very_small_eyes()
ylibka()
sd.pause()
