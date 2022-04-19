import simple_draw



screen_w = 640
screen_h = 480
simple_draw.caption = "Wall"
simple_draw.set_screen_size(screen_w, screen_h)



def brick(x, y, w, h):

    p1 = simple_draw.get_point(x, y)
    p2 = simple_draw.get_point(x + w, y + h)

    simple_draw.rectangle(p1, p2, simple_draw.COLOR_DARK_RED, 0)

    simple_draw.rectangle(p1, p2, simple_draw.COLOR_WHITE, 4)


brick_w = 100
brick_h = 50
brick_start_x = [0, -brick_w // 2]
brick_start_x_idx = 0

brick_y = 0
while brick_y < screen_h:
    brick_x = brick_start_x[brick_start_x_idx]
    while brick_x < screen_w:
        brick(brick_x, brick_y, brick_w, brick_h)
        brick_x += brick_w
    brick_y += brick_h
    brick_start_x_idx = not brick_start_x_idx

simple_draw.pause()
