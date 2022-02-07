import random


# Функция
def str(ss, ww):
    space = " "
    spaces = ""
    # Проверка условии
    if len(ss) >= ww:
        print(s)
    else:
        for i in range((ww - len(ss)) // 2):
            spaces += space
        # Вывод
        print(spaces + ss)


# Пример вывода нескольких строк в окнах разной ширины
for i in range(10):
    s = "Добро пожаловать!"
    w = random.randint(1, 100)
    str(s, w)

# OK