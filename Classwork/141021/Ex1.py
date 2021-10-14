cash = int(input())
tax = cash * 0.18
tips = cash * 0.18
total_cash = tax + tips  + cash
print('Your tax =', '%.2f' % tax)
print('Your tax =', '%.2f' % tips)
print("Your voucher", "%.2f" % total_cash)
