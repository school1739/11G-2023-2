a=int(input())
if a==0:
    print("OSHIBKA")
else:
    b=a
    c=0
    while a!=0:
        a=int(input())
        b=b+a
        c=c+1
    print(b/c)