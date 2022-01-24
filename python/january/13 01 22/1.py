import simple_draw as sd


def puzyirik(point, step, colour):
    radius = 50
    for i in range(3):
        radius -= step
        sd.circle(center_position=point, radius=radius, color=colour, width=1)


point = sd.get_point(300, 550)
COLOR_WHITE = (255, 255, 255)
radius = 50
for i in range(3):
    radius -= 5
    sd.circle(center_position=point, radius=radius, color=COLOR_WHITE, width=1)

for x in range(100, 1001, 100):
    point = sd.get_point(x, 450)
    puzyirik(point=point, step=5, colour=(255, 255, 255))

for y in range(100, 301, 100):
    for x in range(100, 1001, 100):
        point = sd.get_point(x, y)
        puzyirik(point=point, step=5, colour=(255, 255, 255))

for m in range(100):
    point = sd.random_point()
    colour = sd.random_color()
    puzyirik(point=point, step=5, colour=colour)
sd.pause()