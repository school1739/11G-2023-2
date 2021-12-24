### Задание №1
##
# Есть список песен группы Depeche Mode со временем звучания с точностью до долей минут
#
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

# Распечатаем общее время звучания трех песен: 'Halo', 'Enjoy the Silence' и 'Clean' в формате
#   Три песни звучат ХХХ.XX минут

Halo = violator_songs[3]
dlitelnost_Halo = Halo[1]
E_t_S = violator_songs[5]
dlitelnost_E_t_S = E_t_S[1]
Clean = violator_songs[8]
dlitelnost_Clean = Clean[1]
all_dlitelnost = round(dlitelnost_Clean + dlitelnost_Halo + dlitelnost_E_t_S, 2)
print("Три песни звучат", all_dlitelnost, "минут")
# Есть словарь песен группы Yellow со временем звучания с точностью до долей минут
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

# Распечатаем общее время звучания трех песен: 'On Track', 'To the Sea' и 'Beyond Mirrors'
#   А другие три песни звучат приблизительно ХХХ минут

O_T = pocket_universe_songs['On Track']
T_t_S = pocket_universe_songs['To the Sea']
B_M = pocket_universe_songs['Beyond Mirrors']
dlitelnost = round(O_T + T_t_S + B_M)
print("А другие три песни звучат приблизительно", dlitelnost, "минут")

# Evaluation: OK