regim = input("Зашифровать - 1, Расшифровать - 2: ")
alphabet_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alphabet_EU = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'

from itertools import cycle

user_str = list(input("Слово(а) для шифровки(без пробелов!): ").upper())
key_word = list(input("Слово(а) ключ(без пробелов!): ").upper())

if user_str[0] in alphabet_RU:  # Узнаём язык слова
    alphabet = alphabet_RU
    print("Язык - русский")
else:
    alphabet = alphabet_EU
    print("Язык - английский")
# Узнаем индексы букв введенного слова и слова-ключа
index_key_w = []
index_user_w = []
for i in key_word:
    if i != " ":
        index_key_w.append(alphabet.index(i) + 1)
    else:
        index_key_w.append(0)
for i in user_str:
    if i != " ":
        index_user_w.append(alphabet.index(i) + 1)
    else:
        index_user_w.append(0)

def encryption(alphabet):  # Функция для шифровки
    new_index = []
    for old, new in enumerate(cycle(index_key_w)):  # Высчитываем новый индекс для зашифрованной буквы
        if old >= len(user_str):
            break
        new_index.append(index_user_w[old] + new)
    return new_index

encryption_word = ''.join([alphabet[char - 1] for char in encryption(alphabet)])

def decryption(encryption_word, alphabet):  # Функция для расшифровки
    index_encryption_word = []
    for i in encryption_word:  # Узнаем индексы букв зашифрованного слова
        index_encryption_word.append(alphabet.index(i) + 1)

    index_decryption_w = []
    for old, new in enumerate(cycle(index_key_w)):  # Высчитываем индекс для расшифрованной буквы
        if old >= len(encryption_word):
            break
        index_decryption_w.append(index_encryption_word[old] - new)
    return index_decryption_w

decryption_word = ''.join([alphabet[char - 1] for char in decryption(encryption_word, alphabet)])

if regim == "1": print(f"Зашифрованное слово: {encryption_word}.")
if regim == "2": print(f"Расшифрованное слово: {decryption_word}")