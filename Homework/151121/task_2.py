##
# Вычисляем наибольший общий делитель двух положительных чисел
#
# Запрашиваем положительные числа у пользователя
n = int(input("Введите первое положительное число: "))
m = int(input("Введите второе положительное число: "))
# Проверяем на ввод неположительных чисел
if n <= 0 or m <= 0:
    print("Ошибка! Введите положительное число")
else:
    # Выбираем меньшее из чисел
    # и задаём в переменную d (наибольший делитель)
    d = min(n, m)
    # Пока числа n или m не делятся на d без остатка
    while n % d != 0 or m % d != 0:
        # Уменьшаем d на единицу
        d -= 1
    # Выводим результат
    print(f"Наибольший общий делитель чисел {n} и {m}: {d}")

# Evaluation: OK