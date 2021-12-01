import math

x = input()
y = input()
x2 = int(x)
y2 = int(y)
x1 = int(x)
y1 = int(y)
b = 0
while str(x) != "":  # пока не введем "" счетчик работает
    xy = int(x)
    yx = int(y)
    a = (xy - x1) * (xy - x1) + (yx - y1) * (yx - y1)
    c = math.sqrt(a)  # находим расстояние с помощью занчений х1 и у1 из прошлого цикла и ху и ух из настоящего
    b = b + c
    x1 = int(x)
    y1 = int(y)
    x = input()
    y = input()
d = (xy - x2) * (xy - x2) + (yx - y2) * (yx - y2)  # растояние от 1 до последней точки
f = math.sqrt(d)
print(b + f)
