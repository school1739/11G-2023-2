
import simple_draw as sd
sd._init()

def blocks():
    sd.background_color = (136, 69, 53)
    start_x = 0
    start_y = 0
    block_width = 100
    block_hight = 50
    row_block_number = 10
    row_number = 10

    width = 3
    for row in range(row_number):
        if row % 2 == 0:
            set = 50
        else:
            set = 0
        for brick in range(row_block_number):
            left_bottom_x = start_x + set + block_width * brick
            left_bottom_y = start_y + block_hight * row
            left_bottom = sd.get_point(left_bottom_x, left_bottom_y)
            right_top_x = left_bottom_x + block_width
            right_top_y = left_bottom_y + block_hight
            right_top = sd.get_point(right_top_x, right_top_y)
            sd.rectangle(left_bottom, right_top, color=sd.COLOR_WHITE, width=width)

def bg_color(): #аммм, не работала функция sd.background_color, ну нарисовал огроменный прямоугольник кирпичного цвета
    color = (136, 69, 53)
    start_point = sd.get_point(0,0)
    end_point = sd.get_point(600, 600)
    width = 0
    sd.rectangle(start_point, end_point, color=color, width= width)
bg_color()

blocks()  #чет криво получилось правда, сверху не прорисовались почему-то:( так и знал, что прораб обманул и стену не достроил:(

sd.pause()
