a=input()
b=0
c=0
while str(a)!="":
    b=b+int(a)
    c=c+1
    if c%8==0:
        print(1-b%2)
        a = input()
        b=0
    else:
        a = input()
if c%8!=0:
    print("ERROR")
