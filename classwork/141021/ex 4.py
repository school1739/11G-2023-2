s1 = float(input())
sum1 = s1+(0.04*s1)
sum2 = sum1+(0.04*sum1)
sum3 = sum2+(0.04*sum2)
n1 = round(sum1)
v1 = round(sum2)
x1 = round(sum3)
m1 = sum1 % 100
m2 = sum2 % 100
m3 = sum3 % 100
print( str(n1) + str(m1) )
print( str(n2) + str(m2) )
print( str(n3) + str(m3) )