a = input()
b = 0
c = 0
while str(a) != "":  # пока не будет пустой строки
    b = b + int(a)  # счетчик
    c = c + 1  # счетчик
    if c % 8 == 0:
        print(1 - b % 2)
        a = input()
        b = 0
    else:
        a = input()
if c % 8 != 0:
    print("ERROR")  # ошибка при неправильном введении чисел

# Evaluation: +-OK. А вот за такое вот оформление и интерфейс юзеры могут и побить.