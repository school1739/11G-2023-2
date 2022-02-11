# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух',
          'роза')

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик',
          'ромашка')

# создайте множество цветов, произрастающих в саду и на лугу
garden_set = set(garden)
meadow_set = set(meadow)

# выведите на консоль все виды цветов
# Объединяем множества с помощью функции union()
union_set = garden_set.union(meadow_set)
print('Все виды цветов:', end=" ")
# Выводим значения множества в виде строки
# с помощью метода join и разделителя ', '
print(', '.join(union_set))

# выведите на консоль те, которые растут и там и там
# Находим пересечение множеств при помощи оператора &
garden_meadow = garden_set & meadow_set
print('Цветы, которые растут и саду, и на лугу:', end=" ")
print(', '.join(garden_meadow))

# выведите на консоль те, которые растут в саду, но не растут на лугу
# Определяем разницу между множествами при помощи оператора —
only_garden = garden_set - meadow_set
print('Цветы, которые растут в саду, но не растут на лугу:', end=" ")
print(', '.join(only_garden))

# выведите на консоль те, которые растут на лугу, но не растут в саду
# Определяем разницу между множествами при помощи оператора —
only_meadow = meadow_set - garden_set
print('Цветы, которые растут на лугу, но не растут в саду:', end=" ")
print(', '.join(only_meadow))

# Evaluation: OK