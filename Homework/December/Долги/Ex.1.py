##
# Составляем словарь словарей расстояний между городами
#
# Создаём функцию для расчёта расстояния на координатной сетке
def dist_cities(town1, town2):
    d_city = ((town1[0] - town2[0]) ** 2 + (town1[1] - town2[1]) ** 2) ** 0.5
    return d_city


# задан словарь координат городов
sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

distances = {}
# Задаём переменные для координат городов
MSK = sites['Moscow']
LND = sites['London']
PAR = sites['Paris']
# Расчитываем расстояния между городами
distance_MSK_LND = dist_cities(MSK, LND)
distance_LND_PAR = dist_cities(LND, PAR)
distance_MSK_PAR = dist_cities(MSK, PAR)
# Создадим новый словарь для каждого города со словарями расстояний до городов
distances['Moscow'] = {}
distances['Moscow']['London'] = distance_MSK_LND
distances['Moscow']['Paris'] = distance_MSK_PAR
distances['London'] = {}
distances['London']['Moscow'] = distance_MSK_LND
distances['London']['Paris'] = distance_LND_PAR
distances['Paris'] = {}
distances['Paris']['Moscow'] = distance_MSK_PAR
distances['Paris']['London'] = distance_LND_PAR
# Выводим результат
print(distances)