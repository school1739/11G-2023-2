#1
print("Введите параметры конверта")
a = int(input())
b = int(input())
print("Введите параметры бумаги")
c = int(input())
d = int(input())
if (a >= c and b >= d) or (a >= d and b >= c):
    print("для введенных данных ДА")
else:
    print("для введенных данных НЕТ")
c = [8, 9, 6, 8, 3, 11, 9]
d = [9, 8, 8, 6, 4, 9, 11]
for i in range(len(c)):
    if (a >= c[i] and b >= d[i]) or (a >= d[i] and b >= c[i]):
        print("для данных", c[i], d[i], "ДА")
    else:
        print("для данных", c[i], d[i], "НЕТ")

#2

print("Введите параметры отверстия")
a = int(input())
b = int(input())
print("Введите параметры кирпича")
c = int(input())
d = int(input())
e = int(input())
if (a >= c and b >= d) or (a >= c and b >= e) or (a >= d and b >= c) or (a >= d and b >= e) or (a >= e and b >= c) or (
        a >= e and b >= d):
    print("для введенных данных ДА")
else:
    print("для введенных данных НЕТ")
c = [11, 11, 10, 10, 2, 2, 3, 3, 6, 6, 5, 5, 11, 11, 6, 6, 3, 3]
d = [10, 2, 11, 2, 10, 11, 5, 6, 3, 5, 6, 3, 3, 6, 11, 3, 6, 11]
e = [2, 10, 2, 11, 11, 10, 6, 5, 5, 3, 3, 6, 6, 3, 3, 11, 11, 6]
for i in range(len(c)):
    if (a >= c[i] and b >= d[i]) or (a >= c[i] and b >= e[i]) or (a >= d[i] and b >= c[i]) or (
            a >= d[i] and b >= e[i]) or (
            a >= e[i] and b >= c[i]) or (
            a >= e[i] and b >= d[i]):
        print("для данных", c[i], d[i], e[i],
        "ДА")
    else:
        print("для данных", c[i], d[i], e[i],
        "НЕТ")

# +-OK. Зачем вводить параметры конверта\кирпича, если всё равно проверка по
# заданному списку?