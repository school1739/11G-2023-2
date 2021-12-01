
my_family = ["Папа" ,"Мама", "Дедушка"]

my_family_height = [
    ['Папа', 185],
    ["Мама", 170],
    ["Дедушка", 175]
]

print("Рост отца - " + str(my_family_height[0][1]))

summa = 0
for i in range(len(my_family_height)):
    summa += my_family_height[i][1]

print("Общий рост моей семьи - " + str(summa))