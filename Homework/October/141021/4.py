a = int(input('Первоначальная сумма деопозита'))
b = a * 0.04 + a # Сумма за 1 год
c = b * 0.04 + b # Сумма за 2 год
d = c * 0.04 + c # Сумма за 3 год
print("%.2f" % b, "%.2f" % c, "%.2f" % d)
