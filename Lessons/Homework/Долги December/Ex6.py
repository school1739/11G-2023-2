meadow_set = set(meadow)
# выведем на консоль все виды цветов
#
union_set = garden_set.union(meadow_set)
for flower in union_set:
    print(flower)
# выведем на консоль те, которые растут и там и там
#
itamitam_set = garden_set & meadow_set
for flower in itamitam_set:
    print(flower)
# выведем на консоль те, которые растут в саду, но не растут на лугу
#
only_in_garden_set = garden_set - meadow_set
for flower in only_in_garden_set:
    print(flower)
# выведем на консоль те, которые растут на лугу, но не растут в саду
#
only_in_meadow_set = meadow_set - garden_set
for flower in only_in_meadow_set:
    print(flower)

# Evaluation: Почему это лежит отдельно?