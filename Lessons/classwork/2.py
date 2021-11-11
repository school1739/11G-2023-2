b=str(input())
a=0
while b !="":
    a=a+int(b)
    b = str(input())
    if b=="":
        break
if a%5>2.5:
    print(a+5-a%5)
else:
    print(a-a%5)