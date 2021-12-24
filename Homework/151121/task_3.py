##
# Программа для подброса монетки "Орёл или решка"
#
# Импортируем модуль random
import random

# Создаём переменную для подсчёта попыток
total = 0
# Задаём цикл на 10 симуляций
for i in range(10):
    # Задаём пустой список для попыток
    attempts = []
    # Задаём цикл с условием, что 3 последних попытки между собой не равны,
    # при создании множества (set) остаются только неповторяющиеся элементы
    while len(attempts) < 3 or len(set(attempts[-3:])) != 1:
        attempts += random.choice(('О', 'Р'))
    # Выводим рандомно выбранные 'О' - орёл или 'Р' - решка, и кол-во попыток
    print(f'{" ".join(attempts)} (попыток: {len(attempts)})')
    # Суммируем количество попыток
    total += len(attempts)
# Выводим среднее значение попыток
print(f'Среднее количество попыток: {total / 10}')

# Evaluation: OK