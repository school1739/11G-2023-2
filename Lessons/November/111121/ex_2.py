cent = str(input()) #первая переменная для начала цикла
k = 0 #сумма
while cent != "": #начало цикла
    k = k + int(cent)
    cent = str(input())
    if cent == "": #почему-то была ошибка, поставил break и вроде норм (если условие выполняется, то цикл останавливается)
        break
print(k)#вывод общей суммы
print((k + (-k % 5)))#формула для округления числа кратного пяти (формулу нашел на форуме:)