print('Введите сумму')
a = int(input())
b = a * 0.04
c = a * 0.18
d = b + c  + a
print('Налог =', '%.2f' % b)
print('Чаевые =', '%.2f' % c)
print("Итог", "%.2f" % d)

# Evaluation: OK