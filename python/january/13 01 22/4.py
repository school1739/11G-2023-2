mounthes = ["Сентябрь", "Октябрь", "Ноябрь", "Декабрь", "Январь", "Февраль", "Март", "Апрель", "Май", "Июнь"]
educational_grant, expenses = 10000, 12000
summ = expenses
number_mounth = 1
print(mounthes[0], ":", expenses, 'рублей')
for i in range(9):
    expenses = expenses * 1.03
    print(mounthes[number_mounth], ":", round(expenses, 2), 'рублей')
    summ = summ + expenses
    number_mounth += 1
print('Студенту надо попросить: ', (summ - educational_grant * 10) // 1 + 1, 'рублей')