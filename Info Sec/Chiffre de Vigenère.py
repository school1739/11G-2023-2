# Напишите программу, шифрующую входящее сообщение с помощью шифра Виженера.
# Шифр Виженера представляет собой шифр Цезаря с переменной величиной сдвига.
# Величину сдвига задают ключевым словом.
# Например слово БАЗА означает последовательность сдвигов исходных букв: 219121912191...

alphabet_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alphabet_EU = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'

# HINT (использовать не обязательно):
# Если буквы A-Z соответствуют числам 0-25, то код Виженера в общем виде выглядит так:
#   Шифрование:
#       Ci=(Pi+Ki) mod 26
#   Расшифровка:
#       Pi=(Ci-Ki+26) mod 26
# C = Cipher Text (зашифрованный текст)
# P = Plain Text (изначальный текст)
# K = Key (ключ)

plain_text = input("PLAIN: ")
key_text = input("KEY: ")
for key_char in key_text:
    key_index = alphabet_RU.find(key_char)
    print(key_index + 1)

for plain_char in plain_text:
    plain_index = alphabet_RU.find(plain_char)
    print(plain_index + 1)

for char in len(plain_text):
    print(alphabet_RU[plain_index+key_index])
