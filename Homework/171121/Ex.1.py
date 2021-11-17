### Задача 1. Таблица умножения
##
# Запрашиваем у пользователя значения
#
min=int(input("Введите минимальное значение: "))
max=int(input("Введите максимальное значение: "))
print('    ', end="") #Чтобы всё красиво стояло
for i in range(min, max+1):
    print("%4d" %i, end="")
print()
# Выводим таблицу
for i in range(min,max+1):
    print("%4d" %i, end="")
    for k in range(min, max+1):
        print("%4d" % (i*k), end="")
    print()