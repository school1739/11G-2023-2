"""Напишите функцию, которая будет принимать в качестве параметров
строку s, а также ширину окна в символах – w. Возвращать функция долж-
на новую строку, в которой в начале добавлено необходимое количество
пробелов, чтобы первоначальная строка оказалась размещена по центру
заданного окна. Новая строка должна формироваться по следующему
принципу:
-> если длина исходной строки s больше или равна ширине заданного
окна, возвращаем ее в неизменном виде;
-> в противном случае должна быть возвращена строка s с ведущими
пробелами в количестве (len(s) – w) // 2 штук.
В вашей основной программе должен осуществляться пример вывода
нескольких строк в окнах разной ширины."""
def ght(s,w):
    s1=""
    if len (s) >=w:
        return(s)
    else:
        for i in range(((w-len(s)) // 2)+1):
            s1=s1+" "
        s1=s1+s
        return(s1)
s=str(input())
w=int(input())
print(ght(s,w))

# +-OK. Ни подсказок, ни комментариев. Буду снижать оценку за такое.