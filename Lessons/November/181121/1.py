a = int(input())
b = 1
c = 0
while a != 0:  # двоичную запись наоборот с единичкой в начале
    print("остаток", a % 2)
    print("результат деления", a // 2)
    b = b * 10 + a % 2
    a = a // 2
while b != 1:  # вывожу число в 1 цикле наоборот без единички на конце
    c = c * 10 + b % 10
    b = b // 10
print(c)  # итоговое двоичное число

# Evaluation: OK