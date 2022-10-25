lphabet_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alphabet_EU = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
key_list = []  # лист для ключа, если понадобиться, его можно будет увеличить на самого себя
print("Выбирите язык, указав его порядковый номер.")
print("1. Русский")
print("2. Английский")
nomer_yazyka = input("Введите номер: ")
answer1 = ""
answer2 = ""
print("Выбирите действие, указав его порядковый номер:")
print("1. Шифровка")
print("2. Дешифровка")
print("3. Шифровка в обе стороны")
variant = input("Ваш выбор: ")
key_text = str.upper(input("Ключ: "))
plain_text = str.upper(input("Текст: "))
for key in key_text:  # преобразуем ключ в список
    key_list += key
if len(key_text) < len(plain_text):  # если длина ключа меньше основного слова, то увеличиваем его на самого себя
    for _ in range((len(plain_text) - len(key_text)) // 2 + 1):
        key_list += key_list
if nomer_yazyka == "1":  # если выбрали русский язык
    if variant == "1":
        for i in range(len(plain_text)):  # смотрим индексы каждой буквы
            plain_index = alphabet_RU.find(plain_text[i])
            key_index = alphabet_RU.find(key_list[i]) + 1
            if plain_text[i] == " ":
                answer1 += " "
            else:
                answer1 += alphabet_RU[plain_index + key_index]  # складываем индыксы
        print("Рузультат:", answer1)  # выводим зашифрованное слово
    # Далее по аналогии  первому примеру
    if variant == "2":
        for i in range(len(plain_text)):
            plain_index = alphabet_RU.find(plain_text[i])
            key_index = alphabet_RU.find(key_list[i]) + 1
            if plain_text[i] == " ":
                answer1 += " "
            else:
                answer1 += alphabet_RU[plain_index - key_index]
        print("Рузультат:", answer1)
    if variant == "3":
        for i in range(len(plain_text)):
            plain_index = alphabet_RU.find(plain_text[i])
            key_index = alphabet_RU.find(key_list[i]) + 1
            if plain_text[i] == " ":
                answer1 += " "
            else:
                answer1 += alphabet_RU[plain_index + key_index]
        print("Рузультат:", answer1)
        for i in range(len(plain_text)):
            plain_index = alphabet_RU.find(plain_text[i])
            key_index = alphabet_RU.find(key_list[i]) + 1
            if plain_text[i] == " ":
                answer2 += " "
            else:
                answer2 += alphabet_RU[plain_index - key_index]
        print("Рузультат:", answer2)
if nomer_yazyka == "2":  # всё то же самое, но для английского языка
    if variant == "1":
        for i in range(len(plain_text)):  # смотрим индексы каждой буквы
            plain_index = alphabet_EU.find(plain_text[i])
            key_index = alphabet_EU.find(key_list[i]) + 1
            if plain_text[i] == " ":
                answer1 += " "
            else:
                answer1 += alphabet_EU[plain_index + key_index]  # складываем индыксы
        print("Рузультат:", answer1)  # выводим зашифрованное слово
    # Далее всё по аналогии  первому примеру
    if variant == "2":
        for i in range(len(plain_text)):
            plain_index = alphabet_EU.find(plain_text[i])
            key_index = alphabet_EU.find(key_list[i]) + 1
            if plain_text[i] == " ":
                answer1 += " "
            else:
                answer1 += alphabet_EU[plain_index - key_index]
        print("Рузультат:", answer1)
    if variant == "3":
        for i in range(len(plain_text)):
            plain_index = alphabet_EU.find(plain_text[i])
            key_index = alphabet_EU.find(key_list[i]) + 1
            if plain_text[i] == " ":
                answer1 += " "
            else:
                answer1 += alphabet_EU[plain_index + key_index]
        print("Рузультат:", answer1)
        for i in range(len(plain_text)):
            plain_index = alphabet_EU.find(plain_text[i])
            key_index = alphabet_EU.find(key_list[i]) + 1
            if plain_text[i] == " ":
                answer2 += " "
            else:
                answer2 += alphabet_EU[plain_index - key_index]
        print("Рузультат:", answer2)
