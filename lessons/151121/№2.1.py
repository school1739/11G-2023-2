 l = []
d = []

kol_vo = int(input("Введите число:) "))
for i in range(0, kol_vo + 1):
    l.append(i)
    d.append(i)

for i in range(0, kol_vo + 1):
    for q in range(0, kol_vo + 1):
        print(str(l[i] * d[q]), end = "\t" )

