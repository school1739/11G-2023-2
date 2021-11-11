n = int(input())
s = 0
k = 0
if n == 0:
    print('Error')
else:
    while n != 0:
        s += n
        k += n
        n = int(input())
    print(s/k)