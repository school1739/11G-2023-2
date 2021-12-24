a = int(input())
b = 0
c = 0
if a == 0:
    print("Error")  # если первое число 0 то error
else:
    while a != 0:  # цикл, пока а не равно 0
        b = b + a  # сумма всех введенных чисел
        a = int(input())
        c = c + 1  # счетчик
    print(b / c)

# Evaluation: OK