a = input()
b = 0
c = 0
d = 0
f = int(a)
for i in range(len(a)):  # цикл, в котором почленно складываем по формуле цифры
    d = f % 10  # цифра, которую считаем с конца
    f = f // 10  # вычеркиваем последнюю цифру
    b = d * (2 ** i)  # считаем формулу
    c = c + b  # счетчик
print(c)