a=int(input()) # вводим число в десятичной системе счисления
result=""
while a!=0: # используем цикл до тех пор пока число не равно 0
    b=a%2
    result= str(b)+ result
    print(a,'// 2',', остаток',a%2)
    a=a//2 # получаем новое число посредством деления на 2

print(result)

# Evaluation: OK