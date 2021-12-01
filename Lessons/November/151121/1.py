a = int(input()) + 1  # т.к range от 0 до а-1, прибавляем 1
for i in range(a):
    print("")
    for j in range(a):  # цикл в цикле, с перемножением 2 переменных
        print(i * j, end="  ")
