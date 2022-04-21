# with open("Thefile.txt", "r") as the_file:
#     line  = the_file.readline()
#     while line:
#         print(line, end="")
#         line=the_file.readline()
# чтение одной строки за одну итерацию
# with open("Thefile.txt", "r") as the_file:
#     content=the_file.read()
#     print(content)
#     print(type(content)) #<class 'str'>
# чтение всего содержимого в одну строку
# with open("Thefile.txt", "r") as the_file:
#     contents= the_file.readlines() # создаёт список строк
#     print(contents)
#     print(type(contents)) #<class 'list'>
#     string1=contents[0]
#     string2=contents[1]
#     print(string1, string2)
#     print(type(string1))
#     print(string1[2:5]) #llo
#     print(contents[1][6:11]) # good
# with open("Thefile.txt", "r") as the_file: # создаём список
#     inputs = list() #
#     user_in=input("Введите текст: ") # ввод строки
#     inputs.append(user_in + "\n") # добавление строки
#     while user_in!="0": #
#         user_in=input("Введите текст: ")
#         inputs.append(user_in + "\n")
#     inputs.pop()# выбрасывает последний элемент списка
#     inputs.pop(1) # выбрасывает элемент с индексом [1]
#     popend = inputs.pop(1)
#     print(inputs)
#     print(popend)
#
# with open("Thefile.txt", "a") as the_file: # открываем файл на добавление
#     for string in inputs: # итерируемся по списку строк
#         the_file.write(string) # записываем каждую строку в файл по очереди
# the_file.close() # закрывем файл
# with open("Thefile.txt", "r") as the_file: # открыве файл на чтение
#     for message in the_file: # итерируемся по списку чтрок в файле
#         print(message, end="") # вывод каждой строки отдельно
the_file.close()