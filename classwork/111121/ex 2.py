c = int(input('цена: '))#принимаем первое значение цены
sum=0
n = ''
while c!=n: #пока значение с не равно пустой строке
    sum+=int(c)
    c = str(input('цена: '))
print(sum)
op = int(5 * round(sum / 5)) #округляем до пяти сумму
print(op)

