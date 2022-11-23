p=13
q=17
n=p*q
dl=(p-1)*(q-1)
e=11
for d in range(1,50):
    if (e*d-1)%dl==0:
        print(e,n)
        print(d,n)