a=int(input())
b=0
c=0
if a==0:
    print("Error")#вывод ошибки при а=0
else:
    while a!=0:#b-сумма вводимых чисел,с-кол-во вводимых чисел
        b=b+a
        a = int(input())
        c=c+1
    print(b/c)