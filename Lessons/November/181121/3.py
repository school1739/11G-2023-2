import random

b = 0
c = 0
for i in range(100):  # цикл, в котором генерируется 100 рандомных чисел
    a = random.randint(1, 100)
    if (a > b):  # задание максимума и вывод обновление
        b = a
        print(a, "Обновление")
        c = c + 1  # счетчик обновлений
    else:
        print(a)
print("Максимум:", b)
print("Кол-во обновлений:", c)

# Evaluation: OK