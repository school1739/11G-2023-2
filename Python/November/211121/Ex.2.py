### Задание 2. Двоичное в десятичное "суммой степеней"
##
# Запрашиваем у пользователя число
#
number = input("Введите число в двоичной СС: ")
dlina_chisla = len(number)
sign = 0
step = 1
result = 0
print(f"Вы ввели число: {number} в двоичной сиситеме счисления и хотите первести его в десятичную.")
print("Для этого переведем его сначала в десятичную вот так:")
print(f"{number}(2)=", end="")
for i in range(0, len(number)):
    result += (int(number[sign]) * (2 ** (dlina_chisla - step)))  # Вычисляем результат
    # Пошагово выводим результат при условии, когда писать плюс, когда равно
    if dlina_chisla - step >= 1:
        print(f"{int(number[sign])}*2^{dlina_chisla - step}+", end="")
    else:
        print(f"{int(number[sign])}*2^{dlina_chisla - step}=", end="")
    # Увеличиваем номер знака и шага
    sign += 1
    step += 1
# Выводим конечный результат
print(result)
print("Ответ:")
print(f"{number}(2)={result}(10)")

# Evaluation: OK