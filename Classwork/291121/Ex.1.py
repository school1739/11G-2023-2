### Задание №1
##
# Есть словарь координат городов
#
sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
moscow = sites["Moscow"]
london = sites["London"]
paris = sites["Paris"]
msc_ldn = ((moscow[0] - london[0]) ** 2 + (moscow[1] - london[1]) ** 2) ** 0.5
prs_msc = ((paris[0] - moscow[0]) ** 2 + (paris[1] - moscow[1]) ** 2) ** 0.5
ldn_prs = ((london[0] - paris[0]) ** 2 + (london[1] - paris[1]) ** 2) ** 0.5

# Выведем результат
distances = {}
distances["Moscow"] = {}
distances["Moscow"]["London"] = (str(msc_ldn) + "km")
distances["Paris"] = {}
distances["Paris"]["Moscow"] = (str(prs_msc) + "km")
distances["London"] = {}
distances["London"]["Paris"] = (str(ldn_prs) + "km")
print(distances)
