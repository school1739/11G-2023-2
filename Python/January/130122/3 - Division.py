### Задание №3
##
#
# Даны целые положительные числа a и b (a > b)
a, b = 179, 37
count=0 # то, сколько раз мы вычитаем
ostatok=a
while ostatok > b:
    ostatok = ostatok - b
    count += 1
print('Целочисленное деление', a, 'на', b, 'даёт', result) # выводим результат