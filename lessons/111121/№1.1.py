n = int(input())
k = 0
c = n
if n == 0:
    print("Ошибка")
while n != 0:
    n = int(input())
    k += 1
    c = c + n
    if n == 0:
        print(c / k)
