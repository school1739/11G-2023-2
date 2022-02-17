"""Написать программу, где две функции -- "Игрок 1" и "Игрок 2"
играют в игру, а третья функция -- "Судья" -- следит за ходом игры
и ведёт счёт.

Правила игры:
Оба игрока кажый раунд выдают случайное целое число
в некотором диапазоне. Судья сравнивает эти числа и начисляет игрокам очки:
Если числа равны, оба игрока получают 1 очко (+1). Когда число одно из игроков
больше другого, игрок, который выдал большее число, получает 1 очко (+1),
другой игрок штрафуется на 1 очко (-1). Игра продолжается до тех пор, пока
один из игроков не наберёт 50 очков, но не более 100 раундов."""

"""UPDATE 1:
Режим "Читера": после 3 проигрышей увеличивается вероятность "чита".
Чит: увеличение randint range на (+1000, +1000).
Изначальная вероятность считерить: 0%. Увеличение вероятности: +5%.
После первой победы с читом чит отключается. Вероятность чита сохраняется."""