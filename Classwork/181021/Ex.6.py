print('Введите значение')
a=int(input())
if a==130:
    print('Отбойный молоток')
elif 130>a>106:
    print('Между отбойным молотком и гозонокосилкой')
elif a==106:
    print('Гозонокосилка')
elif 106>a>70:
    print('Между гозонокосилкой и будильником')
elif a==70:
    print('Будильник')
elif 70>a>40:
    print('Между будильником и тихой комнатой')
elif a==40:
    print('Тихая комната')
else:
    print("Ошибка")