n=int(input())
x=int(input())
c = n * 0.10
h = x * 0.25
t = round(c)
m = round(h)
d = (c+h) % 100
print( str(m) + str(t) + str(d) + '₽' )

# Evaluation: OK