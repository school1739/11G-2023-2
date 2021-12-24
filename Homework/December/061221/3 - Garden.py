# в саду сорвали цветы
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
all_the_flowers = garden_set | meadow_set
print(' '.join(all_the_flowers))
# выведите на консоль те, которые растут и там и там
# TODO здесь ваш код
itamitam = garden_set & meadow_set
print(' '.join(itamitam))
# выведите на консоль те, которые растут в саду, но не растут на лугу
# TODO здесь ваш код
garden_meadow = garden_set - meadow_set
print(' '.join(garden_meadow))
# выведите на консоль те, которые растут на лугу, но не растут в саду
# TODO здесь ваш код
meadow_garden = meadow_set - garden_set
print(' '.join(meadow_garden))

# Evaluation: OK. Не забывай удалять TODO!