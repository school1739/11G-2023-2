f = open('24-1.txt')
s = f.readline()
count = 1  # количество знаков, идущих без повторов
max_count = 1  # максимальное количество таких знаков
last_sign = 0  # предыдущий знаук
current_sign = 0  # текущий знак
# цикл для перебора знаков в файле
for i in range(len(s)):
    current_sign = s[i]
    # сравниваем знаки и выполняем соответсвующее результату действие
    if current_sign != last_sign:
        count += 1
    else:
        count = 1
    # проверяем максимальный показатель
    if max_count >= count:
        max_count = max_count
    else:
        max_count = count
    last_sign = s[i]
# выводим результат
print(max_count)