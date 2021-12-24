### Задание 3. Подбрасываем монетку
##
#
import random
counter=0
coin=5
previous_coin=7
attempts=0
sum_attempts=0
for i in range(10): # Делаем 10 серий
    # Повторяем, пока не выпадет 3 одинакрых значения
    while counter<2:
        coin= random.randint(0,1)
        # Какое значение выводим на экран
        if coin==0:
            print("Р", end=" ")
        else:
            print("О", end=" ")
        # Увеличиваем счётчик или обнуляем, в зависимости от того, совпадает значение с предыдущим или нет
        if coin==previous_coin:
            counter+=1
        else:
            counter=0
        previous_coin=coin
        attempts+=1 # Складываем количество попыток
    print("(попыток:",attempts,')')  # Выводим количсетво попыток
    coin=5
    previous_coin=7
    sum_attempts+=attempts # Складываем общее число попыток
    counter=0
    attempts=0
print("Среднее количество попыток:",sum_attempts/10) # Выводим среднее количество попыток


# Evaluation: OK