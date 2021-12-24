year = int(input("Введите возраст ")) #ну снова переменная для начала работы цикла
all_sum = 0 #сумма всех билетов

while year != 0: #начало цикла
    if year > 3 and year <= 12: all_sum += 150
    elif year >= 65: all_sum += 250              #просто условия на проверку возраста:цены
    elif year > 12 and year < 65: all_sum += 450
    year = int(input("Введите возраст "))
sd = all_sum // 1000 #считаем количество тысяч в сумме

print("Общая стоимость всех билетов = " + str(all_sum))#вывод суммы
print("Сдача с ближайшей тысячи = "+ str((((sd + 1) * 1000) - all_sum)))# вывод сдачи:)

# Evaluation: OK