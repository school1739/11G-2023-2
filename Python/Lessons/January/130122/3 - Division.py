# Даны целые положительные числа a и b (a > b)
# Определить результат целочисленного деления a на b, с помощью цикла while,
# __НЕ__ используя стандартную операцию целочисленного деления (// и %)
# Формат вывода:
#   Целочисленное деление ХХХ на YYY дает ZZZ
q = 0
a, b = 179, 37
while a > b:
    a = a - b
    q += 1
print(q)

# +-OK. Посчитано верно, но вывод не отформатирован как в задании.
# В следующий раз не засчитаю.