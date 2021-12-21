
l = []
d = []

kol_vo = int(input("Числа в каком диапазоне надо перемножиь? введите число:) "))#
for i in range(0, kol_vo + 1):
    l.append(i)
    d.append(i)

for i in range(0, kol_vo + 1): #цикл для kol_vo столбцов
    for q in range(0, kol_vo + 1): #цикл для kol_vo строк:)
        print(str(l[i] * d[q]), end = "\t" )
    print()