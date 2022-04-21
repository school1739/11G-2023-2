#ith open("TheFile.txt", "r") as the_file:
#    line = the_file.readline()
#    while line:
#       print(line, end="")
#        line = the_file.readline()
#with open("TheFile.txt", "r") as the_file:
#   content = the_file.read()
#   print(content)
#   print(type(content)) # >>> <class'str'>
# чтение всего файла в тодну сторону
with open("The_File.txt", "r") as the_file:
#    contents = the_file.readlines() #Создаёт список строк
#    print(contents)
#    print(type(contents)) # >>> <class'list'>
#    string1 = contents[0]
#    string2 = contents[1]
#    print(string1, string2)
#    print(type(string1)) # >>> <class 'str'>
#    print(string1[2;5]) # >>> llo
#    print(contents1[1][6:10]) # >>> full
inputs = list() # Создаем список для будущих строк
user_input = input("Введите что-нить: ") # Ввод строки
inputs = list() # Добавление ввепденной строки в список

while user_input != "0": #Продолджать ввод, пока не будеть введен "0"
    user_input = input("Введите что-нить: ") # Ввод строки снова
    inputs.append(user_input + "\n") #Добавление введенной строки в список
inputs.pop() # Выбрасывает последний элемент списка
inputs.pop(1) # Выбрасывает элемент под индексом [1]
popped = inputs.pop(1) # Записывает элемент в новую переменную и выбрасывает
                        # из списка
print(inputs)