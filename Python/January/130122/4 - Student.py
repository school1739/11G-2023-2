# Месяцы
mounthes = ["Сентябрь", "Октябрь", "Ноябрь", "Декабрь", "Январь", "Февраль", "Март", "Апрель", "Май", "Июнь"]

# Ежемесячная стипендия, расходы на проживание
educational_grant, expenses = 10000, 12000

sum = expenses
number_mounth = 1
mounth = 10

# Расходы в первый месяц: Сентябрь
print(mounthes[0], "-", expenses, 'рублей')

# Цикл расчетов
for i in range(2, mounth + 1):
    expenses = expenses * 1.03
    print(mounthes[number_mounth], "-", round(expenses, 2), 'рублей')  # Вывод расхотов
    sum = sum + expenses
    number_mounth += 1

# Вывод
print('Студенту надо попросить: ', (sum - educational_grant * mounth) // 1 + 1, 'рублей')
