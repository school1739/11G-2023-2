
n = int(input())
m = int(input())
d = min(n,m) #  Меньший из двух чисел
if n <= 0 or m <= 0: # Проверка на отрицательной
    print('Error')
else:
    while n % d !=0 or m % d !=0: # Наибольший общий делитель
        d -= 1
    print(d)
