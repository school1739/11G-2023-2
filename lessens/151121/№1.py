year = int(input("Введите возраст "))
all_sum = 0

while year != 0:
    if year > 3 and year <= 12: all_sum += 150
    elif year >= 65: all_sum += 250
    elif year > 12 and year < 65: all_sum += 450
    year = int(input("Введите возраст "))
sd = all_sum // 1000

print("Общая стоимость всех билетов = " + str(all_sum))
print("Сдача с ближайшей тысячи = "+ str((((sd + 1) * 1000) - all_sum)))