m=int(input())
n=int(input())
while m!=n:
    if m>n:
        m-=n
    else:
        n-=m
print(n)
