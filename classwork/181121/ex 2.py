a=int(input()) #вводим число
a1=a #запоминаем число в другой переменной
result=0
i=0
while a!=0:
    b=a%10 #запоминаем последнее число
    print(b,'* 2 ^',i,end='')
    result=result+b*2**i # выводим результат операции
    i+=1
    a=a//10 # выводим новое число без последней цифры
    if a != 0:
        print(' +', end=' ')
print(' = ')
i=0
while a1!=0:
    b=a1%10 #запоминаем последнее число
    print(b*2**i,end='')
    i+=1
    a1=a1//10 # выводим новое число без последней цифры
    if a1!=0:
        print(' +',end=' ')
print(' = ',result)

# Evaluation: +-OK. В первой строке пусто после знака "=".