# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
moscow=sites["Moscow"]
london=sites["London"]
paris=sites["Paris"]
msc_ldn=((moscow[0]-london[0])**2+(moscow[1]-london[1])**2)**0.5


distances={}
distances["Moscow"]={}
distances["Moscow"]["London"]=(str(msc_ldn)+"km")

# TODO здесь заполнение словаря

print(distances)