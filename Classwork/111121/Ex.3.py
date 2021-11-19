import math
x1=input()
y1=input()
x2=input()
y2=input()
P=0
first_X=x1
first_Y=y1
while x1!="" or y2!="" or x2!="" or y2!="":
    if x2=="" or y2=="":
        x2 = int(first_X)
        y2 = int(first_Y)
        break
    dlina = abs(math.sqrt((int(x2) - int(x1))**2 + (int(y2) - int(y1))**2))
    P=P+dlina
    x1 =int(x2)
    y1 = int(y2)
    x2=input()
    y2=input()
dlina =  math.sqrt((int(first_X) - int(x1)) ** 2 + (int(first_Y) - int(y1)) ** 2)
P=P+dlina
print("%.2f" %P)