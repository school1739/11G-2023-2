
age = int(input()) # Возраст
s = 0
while age!="":
    if age <=2:
        s +=0
    elif 3<=age<=12:
        s+=150
    elif 13<=age<=65:
        s+=450
    else:
        s+=250
    age = int(input())
print(s) # Результат