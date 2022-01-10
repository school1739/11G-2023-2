import random
k = 0
l = []
l1 = []
for i in range(1, 101):
    l.append(i)
while k != 5:
    rand = random.choice(l)
    l1.append(rand)
    if rand > max(l1):
        print(str(rand) + " <== Обновление")#не пишет "обновление"  не знаю в чем ошибка, будто просто игнорирует условие
        k += 1

    elif rand == 100:
        print(rand)
        break
    else:
        print(rand)

print("> Максимальное значение в ряду: 100>")
print("Количество смен максимального значения: 5")
# не особо рабочий код и нет идей для решения:(

# Evaluation: NOT OK. Печалька.
# Кстати, если тебя утешит, точно такой же код я видел ещё раз или два. И всем было норм.