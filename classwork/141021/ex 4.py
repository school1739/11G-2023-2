s1 = float(input())
sum1 = s1+(0.04*s1)
sum2 = sum1+(0.04*sum1)
sum3 = sum2+(0.04*sum2)
sum1 = float('{:.2f}'.format(sum1))
sum2 = float('{:.2f}'.format(sum2))
sum3 = float('{:.2f}'.format(sum3))
print(sum1)
print(sum2)
print(sum3)

# Evaluation: OK