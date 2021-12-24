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
        print(str(rand) + " <== Обновление")
        k += 1

    elif rand == 100:
        print(rand)
        break
    else:
        print(rand)

print("> Максимальное значение в ряду: 100>") # Хорошая попытка
print("Количество смен максимального значения: 5")

# Evaluation: NOT OK