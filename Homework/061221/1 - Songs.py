# Есть список песен группы Depeche Mode
# со временем звучания с точностью до долей минут

violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]

# Распечатайте общее время звучания трех песен:
# 'Halo', 'Enjoy the Silence' и 'Clean' в формате
#   Три песни звучат ХХХ.XX минут
# Точность указывается в функции round(a, b)
# где a, это число которое надо округлить, а b количество знаков после запятой
# более подробно про функцию round смотрите в документации
# https://docs.python.org/3/search.html?q=round

# Суммируем время звучания песен
# и округляем до точности 2 знака после запятой
time1_three_songs = round(
    violator_songs[3][1] + violator_songs[5][1] + violator_songs[8][1], 2
)
# Выводим результат
print(f'Три песни звучат {time1_three_songs} минут')

# Есть словарь песен группы Yellow
# со временем звучания с точностью до долей минут
pocket_universe_songs = {
    'Solar Driftwood': 1.85,
    'Celsius': 5.98,
    'More': 6.65,
    'On Track': 5.55,
    'Monolith': 6.35,
    'To the Sea': 5.77,
    'Magnetic': 5.88,
    'Liquid Mountain': 2.97,
    'Pan Blue': 5.52,
    'Resistor': 7.22,
    'Beyond Mirrors': 5.82,
}

# Распечатайте общее время звучания трех песен:
# 'On Track', 'To the Sea' и 'Beyond Mirrors'
#   А другие три песни звучат приблизительно ХХХ минут

# Создаём переменные со значениями времени звучания песен
time_song_1 = pocket_universe_songs['On Track']
time_song_2 = pocket_universe_songs['To the Sea']
time_song_3 = pocket_universe_songs['Beyond Mirrors']

# Суммируем и округляем общее время звучания песен
time2_three_songs = round(time_song_1 + time_song_2 + time_song_3)
# Выводим результат
print(f'А другие три песни звучат приблизительно {time2_three_songs} минут')

# Обратите внимание, что делать много вычислений внутри print() - плохой стиль.
# Лучше заранее вычислить необходимое, а затем в print(xxx, yyy, zzz)
