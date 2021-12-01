### Задание №5
##
# Создадим списки:
#
# моя семья
my_family = ["Мария", "Александр", "Алина"]
# список списков приблизителного роста членов вашей семьи
my_family_height = [
    [my_family[0], 171],
    [my_family[1], 185],
    [my_family[2], 162]

]
relatives_mum = my_family_height[0]
relatives_dad = my_family_height[1]
relatives_granny = my_family_height[2]
# Выведем на консоль рост отца
print('Рост отца -', relatives_dad[1], "см")
# Выведем на консоль общий рост вашей семьи как сумму ростов всех членов
print("Общий рост семьи -", relatives_dad[1] + relatives_mum[1] + relatives_granny[1], "см")
