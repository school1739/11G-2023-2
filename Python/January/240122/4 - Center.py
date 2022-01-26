### Задание №4 "Center"
##
#
import random


# функция для выводы строки нужным кол-вом пробелов
def stroka(sp, wn):
    space = " "
    spaces = ""
    # проверяем условие: длина строки больше размера окна
    if len(sp) >= wn:
        print(s)
    else:
        for i in range((wn - len(sp)) // 2):
            spaces += space
        print(spaces + sp)  # вывод результата


# пример вывода нескольких строк в окнах разной ширины
for _ in range(5):
    s = "Привет! Как дела?"
    w = random.randint(1, 500)
    stroka(s, w)
