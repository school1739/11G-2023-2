import random
def taxi(km):
    km = km * 1000
    cost = km // 150 #сколько раз проехали 150 метров
    r = random.uniform(1, 2.5)
    print(r * ( 4 + (cost * 0.25)))
taxi(int(input("Введите км: ")))
