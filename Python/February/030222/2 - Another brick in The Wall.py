### Задание №2 "Another brick in The Wall"
##
#
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50

sd.set_screen_size(500, 500)
# первый вид рядов кирпичей
for i in range(55, 501, 110):
    for m in range(50, 501, 100):
        point = [m, i]
        left_bottom_2 = sd.get_point(point[0] - 55, point[1] - 30)
        right_top_2 = sd.get_point(point[0] + 55, point[1] + 30)
        sd.rectangle(left_bottom_2, right_top_2, color=(127, 127, 0), width=0)  # как бы слой цемента
        left_bottom = sd.get_point(point[0] - 50, point[1] - 25)
        right_top = sd.get_point(point[0] + 50, point[1] + 25)
        sd.rectangle(left_bottom, right_top, color=(127, 63, 0), width=0)  # сами кирпичи
# второй вид рядов кирпичей
for i in range(0, 501, 110):
    for m in range(0, 501, 100):
        point = [m, i]
        left_bottom_2 = sd.get_point(point[0] - 55, point[1] - 30)
        right_top_2 = sd.get_point(point[0] + 55, point[1] + 30)
        sd.rectangle(left_bottom_2, right_top_2, color=(127, 127, 0), width=0)  # как бы слой цемента
        left_bottom = sd.get_point(point[0] - 50, point[1] - 25)
        right_top = sd.get_point(point[0] + 50, point[1] + 25)
        sd.rectangle(left_bottom, right_top, color=(127, 63, 0), width=0)  # сами кирпичи

sd.pause()
