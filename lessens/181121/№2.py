
n = input("Введите число")
l = list(n)
l = l[::-1]
k = len(l) - 1
q = 0
for i in range(len(l)):
    j = int(l[k]) * 2**k
    q = q + j
    k -= 1
print(q)