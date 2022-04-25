#with open("TheFile.txt", "r") as the_file:
#    line = the_file.readline()
#    while line:
#        print(line, end="")
#        line = the_file.readline()
# Чтение одной строки за одну итерацию цикла.

#with open("TheFile.txt", "r") as the_file:
#   content = the_file.read()
#   print(content)
#   print(type(content))  # >>> <class 'str'>
# Чтение всего содерожимого файла в одну строку

with open("TheFile.txt", "r") as the_file:
    content = the_file.read()
    print(content)
    print(type(content))  # >>> <class 'list'>
    string1 = content[0]
    string2 = content[1]
    print
