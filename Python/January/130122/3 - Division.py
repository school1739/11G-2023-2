### Задание №3 "Division"
##
#
# Даны целые положительные числа a и b (a > b)
f, t = 179, 37
count=0 # то, сколько раз мы вычитаем
ostatok=f
while ostatok > t:
   ostatok = ostatok - t
   count += 1
print('Целочисленное деление', f, 'на', t, 'даёт', count) # выводим результат

# OK