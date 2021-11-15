n = int(input())
k = 0 #счетчик
m = 0 #счетчик
if n == 0:
    print("Error")
while n != 0: #создание цикла (при n == 0 цикл останавливается)
    m = m+n
    n = int(input())
    k = k+1
print(m/k) #вывод результата