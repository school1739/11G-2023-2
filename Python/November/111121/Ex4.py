
age = int(input()) # Возраст
s = 0
while age!="":
    if age <=2:
        s +=0
    elif 3<=age<=12:
        s+=150
    elif 13<=age<=65:
        s+=450
    else:
        s+=250
    age = int(input())
print(s) # Результат

# Evaluation: NOT OK. Бесконеченый цикл
# 1
# 43
# 23
# 89
# 0
# 43
# амвы
# Traceback (most recent call last):
#   File "/Homework/November/111121/Ex4.py", line 13, in <module>
#     age = int(input())
# ValueError: invalid literal for int() with base 10: 'амвы'