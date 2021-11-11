c = int(input('цена: '))
sum=0
while c !='':
    sum+=c
    c = int(input('цена: '))
    if (c % 5 ==0 ) and (c % 5 < 2.5):
         print(int(c))
    elif (c % 5 ==0 ) and (c % 5 > 2.5):
        print(round(c))

