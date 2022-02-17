a=open('27-B_demo.txt')
b=a.readlines()
l=0
for i in range(60000):
    c=0
    d=0
    while b[i][c]!=' ':
        d=int(b[i][c])+d*10
        c=c+1
    print(d)
    c=c+1
    f=0
    for j in range(len(b[i])-c-1):
        f = int(b[i][c]) + f * 10
        c = c + 1
    print(f)
    if f>d:
        l=l+d
    else:
        l=l+f
    print(l)
#Задание 27 № 27889, получилось число, которое не делится на 3, если не так, можно с помощью while пойти в
#обратную сторону, пока l%3!=0, или подобрать вручную(ответ правильный)