a = int(input('Введите возраст человека')) # Подразумевается введение целого числа
if a <= 2 and not a < 0:
    print(a * 10.5)
elif a > 2:
    print((a - 2) * 4 + 21)
else:
    print('Error')