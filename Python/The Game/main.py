import random
# целая куча переменных, необходимых для счёта
# числа игроков
p1_number = 0
p2_number = 0
# счётчик очков игорков
count_1 = 0
count_2 = 0
# счётчик раундов
rounds = 0
# счётчик проигрышей
fails_1 = 0
fails_2 = 0
# счётчик читов
cheat_1 = 0
cheat_2 = 0
# переменные для рандома первого и второго игрока
x_0 = -1000
x_1 = 1000
y_0 = -1000
y_1 = 1000

# функция для первого игрока
def p1():
    global p1_number
    global x_0
    global x_1
    p1_number = random.randint(x_0, x_1)
    return p1_number

# функция для второго игрока
def p2():
    global p2_number
    global y_0
    global y_1
    p2_number = random.randint(y_0, y_1)
    return p2_number

# функция для судьи
def judge():
    global p1_number
    global p2_number
    global count_1
    global count_2
    global fails_1
    global fails_2
    # изменение показателей очков, в зависимости от выпонения условия
    if p1_number == p2_number:
        count_1 += 1
        count_2 += 1
    elif p1_number > p2_number:
        count_1 += 1
        count_2 -= 1
        fails_2 += 1
    else:
        count_1 -= 1
        count_2 += 1
        fails_1 += 1
    # вывод очков
    print("Первый игрок: ", count_1)
    print("Второй игрок: ", count_2)

# условие для выполнения цикла
while count_1 != 50 and count_2 != 50 and rounds != 100:
    # проверяем кол-во проиграшей, увеличиваем показаетль чита
    if fails_1 == 3:
        cheat_1 += 5
        fails_1 = 0
    elif fails_2 == 3:
        cheat_2 += 5
        fails_2 = 0
    # проверяем условие для работы чита
    if cheat_1 >= random.randint(5, 100):
        x_0 += 1000
        x_1 += 1000
    elif cheat_2 >= random.randint(5, 100):
        y_0 += 1000
        y_1 += 1000
    # собственно, сама игра
    judge()
    p1()
    p2()
    rounds += 1
# в зависимости от результатов, выводим победителя
if count_1 == count_2:
    print("Победила дружба")
elif count_2 < count_1:
    print("Победил первый игрок")
else:
    print("Победил второй игрок")