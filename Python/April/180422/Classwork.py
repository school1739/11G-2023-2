# Working with files
#
#
# my_file=open("TheFile.txt", "w" )  #read, write, append, binary
# # my_file.write("Hello, world!")
# my_file.close()
# with open("TheFile.txt", "a") as my_file:
#     my_file.write("\nHello again, world!")
#
# my_file.close()
# with open("TheFile.txt", "a") as my_file:
#     my_file.readlines()
#     my_file.readline(5)
# with open("TheFile.txt", "a") as my_file2:
#     print("Hello 3", file=my_file2)
# with open("TheFile.txt", "r") as my_file:
#     for line in my_file:
#         print(line, end="")
# with open("TheFile.txt", "r") as my_file:
#     string1=my_file.readline()
#     print(string1, end="")
#     string2=my_file.readline()
#     print(string2)
# with open("TheFile.txt", "r") as my_file:
#     line=my_file.readline()
#     while line:
#         print(line[0:5], end="\n")
#         line=my_file.readline()
# with open("TheFile.txt", "r") as my_file:
#     lines= my_file.readlines()
#     print(lines)
#     for str in lines:
#         print(str, end="")
# with open("TheFile.txt", "r") as my_file:
#     lines = my_file.readlines()
#     lines_set = set(lines)
#     print(lines_set)
