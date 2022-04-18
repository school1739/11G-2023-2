# Working with files

# my_file = open("TheFile.txt", "w")  # r/w/a/b - read, write, append, binary
# # write - ПЕРЕЗАПИСАТЬ весь файл
# # append - ДОБАВИТЬ в конец файла
#
# my_file.write("Hello, world!")

# with open("TheFile.txt", "r") as my_file:
#     print(my_file.readlines()) # Все строки в список строк
#     print(my_file.readline(5)) # ОДна строка до 5 символа

# with open("TheFile.txt", "a") as my_file2:
#     print("Hello 3", file=my_file2)

# with open("TheFile.txt", "r") as my_file:
#     for line in my_file:
#         print(line, end="")

# with open("TheFile.txt", "r") as my_file:
#     string1=my_file.readline() # Прочесть одну строку до указанного знака
#     # Если знак не указан или >len(str), вывести полную строку
#     print(string1, end="")
#     string2=my_file.readline() # Уже содержит итератор
#     # Будет выводить следующую строку каждый запуск
#     print(string2)

# with open("TheFile.txt", "r") as my_file:
#     line=my_file.readline()
#     while line:
#         print(line[10:0:-1], end="\n") # line - строка, для вывода отедльных
#         # частей используем слайсы
#         line=my_file.readline()

# with open("TheFile.txt", "r") as my_file:
#     lines=my_file.readlines()
#     print(lines)
#     for str in lines:
#         print(str[7:1:-2], end="")

with open("TheFile.txt", "r") as my_file:
    lines=my_file.readlines()
    print(lines)
    print(lines[5])
    lines_set=set(lines)
    print(lines_set)

my_file.close()