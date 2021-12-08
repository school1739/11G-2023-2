

import math
x1 = input('Введите первую координату X: ')
y1 = input('Введите первую координату Y: ')
x2 = input('Введите следующую координату X: ')
y2 = input('Введите следующую координату Y: ')
P = 0
fpx=x1
fpy=y1
while x1!='' or y1!='' or x2!='' or y2!='':
    if x2=='' or y2=='':
        x2 = int(fpx)
        y2 = int(fpy)
        break
    length = abs(math.sqrt((int(x2) - int(x1))**2 + (int(y2)) - int(y1))**2)
    p = p + length # периметр
    x1 = int(x2)
    y1 = int(y2)
    # Следующие координаты
    x2 = input()
    y2 = input()
length = math.sqrt((int(fpx) - int(x1)) ** 2 + (int(fpy) -int(y1)) **2)
p = p + length # итоговый периметр
print("%.2f" %p)
