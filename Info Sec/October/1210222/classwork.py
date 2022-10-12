alphabet_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alphabet_EU = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
print("Выбирите язык, указав его порядковый номер.")
print("1. Русский")
print("2. Английский")
nomer_yazyka = input("Введите номер: ")
print("Выбирите действие, указав его порядковый номер:")
print("1. Шифровка")
print("2. Дешифровка")
print("3. Все возможные шифроки")
variant = input("Ваш выбор: ")
if variant == "1" or variant == "2":
    key = int(input("Введите ключ: "))
text = str.upper(input("Введите текст: "))
answer = ''
if nomer_yazyka == "1": # если выбрали русский язык
    if variant == "1":
        for l in text:
            if l == " ":
                answer += " "
            else:
                answer += alphabet_RU[(alphabet_RU.index(l) + key) % len(alphabet_RU)] # получаем ответ
        print("Рузультат:", answer) # выводим ответ
# далее всё аналогично первому примеру
    if variant == "2":
        for l in text:
            if l == " ":
                answer += " "
            else:
                answer += alphabet_RU[(alphabet_RU.index(l) - key) % len(alphabet_RU)]
        print("Рузультат:", answer)
    if variant == "3":
        for i in range(1, 33):
            key = i
            answer = ""
            for l in text:
                if l == " ":
                    answer += " "
                else:
                    answer += alphabet_RU[(alphabet_RU.index(l) + key) % len(alphabet_RU)]
            print("Рузультат:", answer)
if nomer_yazyka == "2":
    if variant == "1":
        for l in text:
            if l == " ":
                answer += " "
            else:
                answer += alphabet_EU[(alphabet_EU.index(l) + key) % len(alphabet_EU)]
        print("Рузультат:", answer)
    if variant == "2":
        for l in text:
            if l == " ":
                answer += " "
            else:
                answer += alphabet_EU[(alphabet_EU.index(l) - key) % len(alphabet_EU)]
        print("Рузультат:", answer)
    if variant == "3":
        for i in range(1, 26):
            key = i
            answer = ""
            for l in text:
                if l == " ":
                    answer += " "
                else:
                    answer += alphabet_EU[(alphabet_EU.index(l) + key) % len(alphabet_EU)]
            print("Рузультат:", answer)
