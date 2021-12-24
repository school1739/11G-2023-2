cent = str(input())
k = 0 #сумма
while cent != "":
    k = k + int(cent)
    cent = str(input())
    if cent == "":
        break
print(k)
print((k + (-k % 5)))

# Evaluation: OK