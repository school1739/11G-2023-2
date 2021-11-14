sum = float(input())
sum_nalog = sum * 0.2
sum_tea = sum * 0.18 # пришлось исправить опечатку здесь
all = sum + sum_nalog + sum_tea
print("{0:.2f}".format(sum_nalog))
print("{0:.2f}".format(sum_tea))
print("{0:.2f}".format(all))

# Evaluation: OK, опечатка в названии переменной в 3 строке, из-за которой программа не работала.
# Пожалуйста, перез коммитом, проверяйте программу.