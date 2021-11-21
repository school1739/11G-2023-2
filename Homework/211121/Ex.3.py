### Задание 3. Смена лидера
##
#
import random
counter=0
number=0
kolichestvo_smen=0
while counter!=1: # Условие для первого числа
    number=random.randint(1,100)
    print(number)
    max_number=number # Первое число делаем максимальным
    counter+=1
while counter!=101:
    number=random.randint(1,100)
    # Если число меньше максимального или равно ему, то мы просто его записываем
    if number<=max_number:
        print(number)
    elif number>max_number:
        # Если новое число больше максимального, то мы его делаем новым максимальным
        print(number,"<== Максимальное число")
        max_number=number
        kolichestvo_smen+=1 # Увеличиваем значение количества смен
    counter+=1
# Выводим искомые значения
print("Максимальное значение в ряду:",max_number)
print("Количество смен максимального значения:",kolichestvo_smen)