kolvo = int(input())
if kolvo < 3 or kolvo > 10:
    print("Вы ввели слишком много сторон")
if kolvo == 3:
    print("Треугольник")
elif kolvo == 4:
    print("Квадрат")
else:
    print("многоугольник")