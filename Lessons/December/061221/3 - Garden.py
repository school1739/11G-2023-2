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
#for i in garden:
#    print(i)
#for i in meadow:
#    print(i)
union_set = garden_set.union(meadow_set)
for i in union_set:
    print(i)
# выведите на консоль те, которые растут и там и там
# TODO здесь ваш код
all_set = garden_set & meadow_set
print('Цветы и там и там')
for i in all_set:
    print(i)
# выведите на консоль те, которые растут в саду, но не растут на лугу
# TODO здесь ваш код
print('Те цветы которые растут в саду но не растут на лугу')
sad_not_sad = garden - meadow
for i in sad_not_sad:
    print(i)
# выведите на консоль те, которые растут на лугу, но не растут в саду
# TODO здесь ваш код
