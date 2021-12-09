##
# Вычисляем значение бита четности для групп из восьми бит, введенных пользователем,
# с использованием контроля четности
#
# Запрашиваем у пользователя пакет данных в виде 8 бит
data_packet = input("Введите 8 бит (1 или 0): ")
# Создаём переменную для индикации ошибки
error_1_0 = 0
# Проверяем на окончание ввода - пустую строку
while data_packet != "":
    # Проверяем символ на неравенство 1 или 0
    for i in data_packet:
        if i != '1' and i != '0':
            error_1_0 = 1
            break
    # Определяем корректность введенных данных
    # на количество символов не равное 8 и индикатор ошибки error_1_0
    if len(data_packet) == 8 and error_1_0 == 0:
        # Определяем чётность бит и выводим соответствующее сообщение для пользователя
        if data_packet.count("1") != 0 and data_packet.count("1") % 2 == 0:
            print("Бит чётности: 1")
        else:
            print("Бит чётности: 0")
        data_packet = input("Введите 8 бит (1 или 0) (Enter для окончания ввода): ")
    else:
        print("Ошибка! Вы ввели не 8 бит или символ не равный 1 или 0!")
        error_1_0 = 0
        data_packet = input("Введите 8 бит (1 или 0) (Enter для окончания ввода): ")
