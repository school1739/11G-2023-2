# Заимствовал идеи для написания данного кода
# в открытых репозитроиях различных пользователей GitHub (не у одноклассников)

l = input("Введите восьмибитный код, содержащий только нули и единицы ")  # введите всоьмибитный код, содержащий
# только нули и единицы

while l != "":  # цикл работает пока не будет введена пустая строка

    if l.count("0") + l.count("1") != 8 or len(l) != 8:  # dumb test
        print("Попробуй ещё разок")  # уведомдение о том что здесь нету 8 символов
    else:
        o = l.count("1")  # считаем количество единиц
        if o % 2 == 0:
            print("Бит четности - 1.")  # бит четности - 1
        else:
            print("Бит четности - 0.")  # бит четности - 0
    l = input("Введите восьмибитный код ")  # повторяем цикл

# Evaluation: OK