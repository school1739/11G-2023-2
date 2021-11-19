age=input()
sum=0
while age!="":
    if int(age)<=2:
        sum+=0
    elif 3<=int(age)<=12:
        sum+=150
    elif 13<=int(age)<=65:
        sum+=450
    else:
        sum+=250
    age=input()
print(sum)