for i in range(1, 1000):
    s = i
    n = 4
    while s < 37:
        s = s + 3
        n = n * 2
    if n == 128:
        print(i)
        break