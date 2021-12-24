a=int(input())
b=int(input())
c=0
d=0
if a>b:#уменьшение памяти путем перебора до наименьшего числа
    for i in range(b):
        c=c+1#счетчик
        if b%c==0 and a%c==0:#проверка
            d=c#при прохождении проверки d=max c, т.к с увеличивается
else:
    for i in range(a):#тоже самое
        c=c+1
        if a%c==0 and b%c==0:
            d=c
print(d)

# Evaluation: OK