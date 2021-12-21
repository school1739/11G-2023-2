import random


counter=0
coin=5
previous_coin=7
attempts=0
sum_attempts=0
for i in range(10):
    while counter<2:
        coin= random.randint(0,1)

        if coin==0:
            print("Р", end=" ")
        else:
            print("О", end=" ")
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