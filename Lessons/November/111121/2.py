b = 0
a = input()
while (str(a) != ''):  # b-сумма введенных чисел, пока не будет пустая строка
    b = b + float(a)
    a = input()
if b % 5 > 2.5:  # округление числа в большую сторону
    print(b)
    print(b + 5 - (b % 5))
else:  # округление числа в меньшую сторону
    print(b)
    print(b - (b % 5))

# Evaluation: OK