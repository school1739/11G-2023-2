

c = input() # Запрашиваем у ползователся цены
s = 0
while c!='': # Пустая строка
    s = s + int(c)
    c = input()
    if c =='': # Непустая строка
        s +=0
print(s) #Сумма всех введенных сум
print(round(s/5.0)*5) # Сумма наличным

# Evaluation: OK