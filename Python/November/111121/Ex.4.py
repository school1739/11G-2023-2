### Задание 4.
##
# Запрашиваем у пользователя возраст человека
#
age = input("Введите возраст: ")
total_price = 0
# Задаём условие, сколько прибавлять к сумме, в зависимости от возраста
while age != "":
    if int(age) <= 2:
        total_price += 0
    elif 3 <= int(age) <= 12:
        total_price += 150
    elif 13 <= int(age) <= 65:
        total_price += 450
    else:
        total_price += 250
    age = input("Введите следующий возраст: ")  # Запрашиваем у пользователя возраст следующего человека
print("Итого: ", total_price)  # Выводим результат

# Evaluation: OK