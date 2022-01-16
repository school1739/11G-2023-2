h=str(input('возраст посетителя : ')) #считаем возраст первого посетителя
m=''
sum=0
while h!=m:
    if int(h)>=0 and int(h)<=2: #от 0 до 2
        sum+=0
    elif int(h)>=3 and int(h)<=12: #от 3 до 12
        sum+=150
    elif int(h)>65: #пенсионеры
        sum+=250
    else:
        sum+=450 #взрослые
    h =str(input('возраст посетителя : ')) #считаем возраст нового посетителя
print(sum)
n=1000
while sum>n:
    n+=1000
print(n-sum) #считаем сдачу

# Evaluation: OK