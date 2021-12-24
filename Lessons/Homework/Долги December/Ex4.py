garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза')

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка')

# создайте множество цветов, произрастающих в саду и на лугу
# garden_set =
# meadow_set =
# TODO здесь ваш код
garden_set = set(garden)
meadow_set = set(meadow)
# выведите на консоль все виды цветов
# TODO здесь ваш код
union_set = garden_set.union(meadow_set)
for flower in union_set:
    print(flower)
# выведите на консоль те, которые растут и там и там
# TODO здесь ваш код
itamitam_set=garden_set & meadow_set
for flower in itamitam_set:
    print(flower)
# выведите на консоль те, которые растут в саду, но не растут на лугу
# TODO здесь ваш код

# выведите на консоль те, которые растут на лугу, но не растут в саду
# TODO здесь ваш код

# Evaluation: А где всё?