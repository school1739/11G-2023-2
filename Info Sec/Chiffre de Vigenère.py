# Напишите программу, шифрующую входящее сообщение с помощью шифра Виженера.
# Шифр Виженера представляет собой шифр Цезаря с переменной величиной сдвига.
# Величину сдвига задают ключевым словом.
# Например слово БАЗА означает последовательность сдвигов исходных букв: 219121912191...

alphabet_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alphabet_EU = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
slovo = input("Слово, которое надо зашифровать - ")
slovo = slovo.upper()
al_ru = []
for i in alphabet_RU:
    al_ru.append(i)

slovo_sp = []
for i in slovo:
    slovo_sp.append(i)

shifr_slovo = []
for i in range(len(slovo_sp)):
    key = int(input("Величина сдвига(для каждой буквы отдельно)- "))
    index = al_ru.index(slovo_sp[i])
    index += key
    shifr_slovo.append(al_ru[index])

print(shifr_slovo)



# HINT (использовать не обязательно):
# Если буквы A-Z соответствуют числам 0-25, то код Виженера в общем виде выглядит так:
#   Шифрование:
#       Ci=(Pi+Ki) mod 26
#   Расшифровка:
#       Pi=(Ci-Ki+26) mod 26