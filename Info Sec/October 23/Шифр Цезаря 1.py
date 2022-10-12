shift = 4 # Сдвиг шифра на 4 символа
text = "SHERLOCK" # Изначальный текст полностью заглавными буквами для демонстрации работы кода
encryption = "" # Выводимый шифр
for c in text: # Условия для заглавного символа в тексте
    # Положение символа в алфавите от 0-25
    c_unicod = ord(c)
    c_index = ord(c) - ord('A')
    # Координирование изначального символа относительно алфавита с учетом указанного сдвига [4]
    new_index = (c_index + shift) % 26 # Шифрлование для символа для английского алфавита (26 символов)
    # Преобразование изначального символа в новый
    new_unicode = new_index + ord('A')
    new_character = chr(new_unicode)
    # Установка в зашифрованной строке
    encryption = encryption + new_character
else: # Условие для строчного символа в тексте
    encryption += c
print("Изначальный текст:", text) # Вывод изначального текста
print("Полученный шифр:", encryption) # Вывод получившегося шифра


 # Дз на сайте https://dvsemenov.ru/shifr-cezarya-na-python-rukovodstvo-po-shifrovaniyu-teksta/#i