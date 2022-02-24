# (определение функций)
import simple_draw as sd

# Задаём размер окна для вывода результата рисования
width = 1200
height = 600
sd.set_screen_size(width, height)
# Написать функцию отрисовки смайлика по заданным координатам
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Под смайликом сделать подпись "Shit happens"

# Создаём словарь координат для букв в подписи "Shit happens"
SYMBOLS = {
    's': [((1, 0.7), (0.5, 1)),
          ((0.5, 1), (0, 0.7)),
          ((0, 0.7), (1, 0.3)),
          ((1, 0.3), (0.5, 0)),
          ((0.5, 0), (0, 0.3))],
    'S': [((2, 1.4), (1, 2)),
          ((1, 2), (0, 1.4)),
          ((0, 1.4), (2, 0.6)),
          ((2, 0.6), (1, 0)),
          ((1, 0), (0, 0.6))],
    'h': [((0, 1), (0, 0)),
          ((0, 0.5), (1, 0.5)),
          ((1, 0.5), (1, 0))],
    'i': [((0.5, 0), (0.5, 0.8)),
          ((0.5, 0.9), (0.5, 1))],
    't': [((0, 1), (1, 1)),
          ((0.5, 1), (0.5, 0))],
    'a': [((0, 0.7), (0.5, 1)),
          ((0.5, 1), (1, 0.7)),
          ((1, 0.7), (1, 0)),
          ((1, 0.5), (0, 0.5)),
          ((0, 0.5), (0, 0)),
          ((0, 0), (1, 0))],
    'p': [((0, 0), (0, 1)),
          ((0, 1), (1, 1)),
          ((1, 1), (1, 0.5)),
          ((1, 0.5), (0, 0.5))],
    'e': [((1, 0.3), (0.5, 0)),
          ((0.5, 0), (0, 0.3)),
          ((0, 0.3), (0, 0.7)),
          ((0, 0.7), (0.5, 1)),
          ((0.5, 1), (1, 0.5)),
          ((1, 0.5), (0, 0.5))],
    'n': [((0, 0), (0, 1)),
          ((0, 0.8), (0.5, 1)),
          ((0.5, 1), (1, 0.8)),
          ((1, 0.8), (1, 0))],
    ' ': []
}


# Функция отрисовки смайлика по заданным координатам и цвету
def drawing_smiley_face(x, y, color):
    # Лицо
    sd.circle(sd.get_point(x, y), 200, color, 0)
    # Глаза
    sd.ellipse(sd.get_point(x - 100, y + 15),
               sd.get_point(x - 50, y + 85),
               sd.COLOR_BLACK)
    sd.ellipse(sd.get_point(x + 50, y + 15),
               sd.get_point(x + 100, y + 85),
               sd.COLOR_BLACK)
    # Улыбка
    sd.ellipse(sd.get_point(x - 100, y - 150),
               sd.get_point(x + 100, y),
               sd.COLOR_BLACK)
    sd.ellipse(sd.get_point(x - 100, y - 135),
               sd.get_point(x + 100, y + 10),
               color)
    # Румянец
    sd.ellipse(sd.get_point(x - 155, y - 75),
               sd.get_point(x - 80, y),
               (255, 0, 0))
    sd.ellipse(sd.get_point(x + 155, y - 75),
               sd.get_point(x + 80, y),
               (255, 0, 0))


# Функция для рисования букв
def drawing_symbol(symb, start, width_s, height_s, depth):
    # Рисуем линии букв с помощью словаря SYMBOLS
    for line in SYMBOLS[symb]:
        line_start = sd.get_point(
            line[0][0] * width_s + start.x,
            line[0][1] * height_s + start.y
        )
        line_end = sd.get_point(
            line[1][0] * width_s + start.x,
            line[1][1] * height_s + start.y
        )
        sd.line(line_start, line_end, sd.COLOR_PURPLE, depth)


# Функция для рисования текста
def drawing_text(text):
    for i, symbol in enumerate(text):
        # Проверяем на заглавную букву
        if symbol.istitle():
            drawing_symbol(
                symbol,
                sd.get_point(70 * i + 200 - 50, 35),
                50, 50, 7)
        else:
            drawing_symbol(
                symbol,
                sd.get_point(70 * i + 200, 35),
                50, 50, 7)


# Рисуем смайлик
drawing_smiley_face(width / 2, height / 2, sd.COLOR_YELLOW)

# Рисуем подпись под смайликом
drawing_text("Shit happens")

sd.pause()
