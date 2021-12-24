### Задание №3
##
# в саду сорвали цветы
#
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза')
# на лугу сорвали цветы
#
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка')
# создадим множество цветов, произрастающих в саду и на лугу
#
garden_set = set(garden)
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

# Evaluation: NOT OK. Что это за вывод отдельных цветов?