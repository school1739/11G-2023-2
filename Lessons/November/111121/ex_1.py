n = int(input()) #первая переменная для начала цикла
k = 0 #счетчик
c = n
if n == 0:
    print("Ошибка")
while n != 0: #создание цикла
    n = int(input())
    k += 1
    c = c + n
    if n == 0: #если выводить среднее арифметическое после каждого ввода, то как-то некрасиво, а если не создавать
               #это условие, то при конечном выводе будет ошибка, поэтому оно здесь:)
        print(c / k)