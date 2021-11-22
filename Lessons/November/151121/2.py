a=int(input())
b=int(input())
c=0
d=0
if a>b:
    for i in range(b):
        c=c+1
        if b%c==0 and a%c==0:
            d=c
else:
    for i in range(a):
        c=c+1
        if a%c==0 and b%c==0:
            d=c
print(d)