c = int(input('цена: '))
sum=0
n = ''
while c!=n:
    sum+=c
    c = int(input('цена: '))
print(sum)
if   c % 5 < 2.5:
     int(c)
elif   c % 5 > 2.5:
    print(round(c))
else:
    print('нельзя расчитать остаток')

