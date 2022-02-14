# (цикл for)
import time # для дебага и если шо-то пойдет не так:)
import simple_draw as sd #первое задание
sd._init()
rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
x1 = 50
x2 = 350
width = 4
shag = 5
for i in range(7):
    start_point = sd.get_point(x1, 50)  #ну тут вроде все и так понятно, шо коментировать не знаю
    end_point = sd.get_point(x2, 450)
    sd.line(start_point, end_point, color=rainbow_colors[i], width=width) #фигачим линию
    x1 += shag
    x2 += shag



# TODO здесь ваш код
start_point_2 = sd.get_point(350, -600) #второе задание
radius = 10
q = 0
for i in range(900, 600, -10):
    sd.circle(start_point_2, radius=i, color=rainbow_colors[q], width=10)#а тут фигачим окружность:)
    q += 1
    if q == 7: #шо бы ошибки не было с несуществующим индексом кортежа:(
        break

sd.pause()
