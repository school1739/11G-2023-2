a=int(input())
result=""
while a!=0:
    b=a%2
    result= str(b)+ result
    print(a,'// 2',', остаток',a%2)
    a=a//2

print(result)