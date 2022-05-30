"""Текстовый файл состоит из символов P, Q, R и S.
Определите максимальное количество идущих подряд символов в прилагаемом файле, среди которых нет идущих подряд символов P.

Reminder:
+ Не забывайте комментировать блоки кода.
+ Отделяйте блоки кода друг от друга пустыми строками.
+ Используйте Ctrl+Alt+L для форматирования.
+ Переменные называем осмысленно (см. PEP8, Function and Variable Names). За названия, не соответстующие PEP8 снижу оценки).
"""

# EGE 24

counter = 1  # the variable to count characters going in a row
max_counter = 1  # the variable to count the max amount of characters going in a row

with open("24.txt", 'r') as file:  # open for reading
    text = file.read()  # read the file

    for letter in range(len(text) - 1):  # use the cycle to check letters

        if text[letter] == "R" or text[letter] == "Q" or text[letter] == "S" or text[letter] == "P" and text[letter + 1] != "P":
            # (above) check requirements of the task
            counter += 1  # increase the counter value
            max_counter = max(max_counter, counter)  # update the information about the max value

        else:
            counter = 1  # otherwise counter is the same

print(max_counter)  # display the max value

# OK