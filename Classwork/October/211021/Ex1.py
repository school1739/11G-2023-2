day = int(input())
month = int(input())
year = int(input())
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print('Высокосный')
else:
    print('Обычный')
if (month == 'Апрель' or month == 'Июнь' or month =='Сентябрь' or month =='Ноябрь') and day == 30:
    new_month = month + 1 # Опечатка в отступе
elif (month == 'Январь' or month =='Март' or month == 'Май' or month =='Июль' or month == 'Август' or month == 'Октябрь' or month == 'Декабрь') and day == 31:
    print('31')
else:
    print('28 и 29')

# Evaluation: OK