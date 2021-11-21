a=int(input())
b=0
c=0
if a==0:
    print("Error")
else:
    while a!=0:
        b=b+a
        a = int(input())
        c=c+1
    print(b/c)