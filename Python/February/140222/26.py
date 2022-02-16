### Задание 26
##
#
f = open("26.txt")
file = f.readlines()
# первая строка
s = file[0].split()
# удаляем первую строку
del (file[0])
# преобразуем в целочисленное значение
for i in range(0, len(file)):
    file[i] = int(file[i])
# сортировка от большего к меньшему
file = sorted(file)
amount = 0
# считаем наибольшее количество файлов пользователей
for m in range(0, len(file)):
    if amount + file[m] <= int(s[0]):
        amount += file[m]
    else:
        break
# выводим наибольшее количество файлов пользователей
print(m)
# находим оставшееся место, после добавления мамксимального количества файлов пользователй
ostatok = int(s[0]) - amount
# находим наибольший файл пользователей в основном фалйе, на который можно заменить наибольший файл в архиве
for k in range(0, len(file)):
    if ostatok + file[m - 1] >= file[k]:
        max_amount = file[k]
    else:
        break
# выводим наибольший размер файла, подходящий по условию
print(max_amount)
