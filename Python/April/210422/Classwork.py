# with open("TheFile.txt", "r") as the_file:
#     line = the_file.readline()
#     while line:
#         print(line, end="")
#         line = the_file.readline()
#         print(type(line))
# Чтение одной строки за одну итерацию цикла.

# with open("TheFile.txt", "r") as the_file:
#     content = the_file.read()
#     print(content)
#     print(type(content))  # >>> <class 'str'>
# Чтение всего содержимого файла в одну строку

# with open("TheFile.txt", "r") as the_file:
#     contents = the_file.readlines()  # Создаёт список строк
#     print(contents)
#     print(type(contents))  # >>> <class 'list'>
#     string1 = contents[0]
#     string2 = contents[1]
#     print(string1, string2)
#     print(type(string1))  # >>> <class 'str'>
#     print(string1[2:5])  # >>> llo
#     print(contents[1][6:10])  # >>> full

inputs = list()  # Создаем список для будущих строк
user_input = input("Введите что-нибудь: ")  # Ввод строки
inputs.append(user_input + "\n")  # Добавление введенной строки в список

while user_input != "0":  # Продолжать ввод пока не будет введен 0
    user_input = input("Введите что-нибудь: ")  # Ввод строки снова
    inputs.append(user_input + "\n")  # Добавление введенной строки в список
inputs.pop()  # Выбрасывает последний элемент списка
inputs.pop(1)  # Выбрасывает элемент под индексом [1]
popped = inputs.pop(1)  # Записывает элемент в новую переменную и выбрасывает
# из списка
print(inputs)
print(popped)

# >>> ['1\n', '4\n', '5\n', '6\n', '7\n', '8\n', '9\n']
# >>> 3

with open("TheFile.txt", "a") as the_file:  # Открываем файл на добавление
    for string in inputs:  # Итерируемся по списку строк (см. выше)
        the_file.write(string)  # Записываем каждую строку в файл по очереди
the_file.close()  # Закрываем файл

with open("TheFile.txt", "r") as the_file:  # Открываем файл на чтение
    for message in the_file:  # Итерируемся по списку строк В ФАЙЛЕ
        print(message, end="")  # Вывод каждой строки отдельно
the_file.close()  # Закрываем файл
