# Напишите программу, шифрующую входящее сообщение с помощью шифра Виженера.
# Шифр Виженера представляет собой шифр Цезаря с переменной величиной сдвига.
# Величину сдвига задают ключевым словом.
# Например слово БАЗА означает последовательность сдвигов исходных букв: 219121912191...

alphabet_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alphabet_EU = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'

print("Выбирите язык, указав его порядковый номер.")
print("1. Русский")
print("2. Английский")
nomer_yazyka = input("Введите номер: ")
if nomer_yazyka =="1":
    key_text = input("KEY: ")
    plain_text = input("PLAIN: ")
    for i in range (len(plain_text)):
        plain_index = alphabet_RU.find(plain_text[i])
        key_index = alphabet_RU.find(key_text[i])+1


