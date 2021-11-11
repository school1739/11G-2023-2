n=int(input())
s=0
k=0
while n !=0:
    s=s+n
    k=k+1
    n = int(input())
print(s/k)
if n == 0:
    print('ошибка')
else:
    print(s/k)