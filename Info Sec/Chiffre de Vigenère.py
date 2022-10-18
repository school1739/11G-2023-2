# Напишите программу, шифрующую входящее сообщение с помощью шифра Виженера.
# Шифр Виженера представляет собой шифр Цезаря с переменной величиной сдвига.
# Величину сдвига задают ключевым словом.
# Например слово БАЗА означает последовательность сдвигов исходных букв: 219121912191...


alf = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
#ну и снова таки, про русский ни слова не было, прошу заметить:) там все тоже  просто, но вместо alf будет alf_1 и alf_2:)
choice = int(input("1 - шифрование, 2 - дешифрование --> "))

def shifr(slovo_key):
    global alf
    slovo_for_shifr = input("Введите слово, которое хотите зашифровать --> ").upper()
    sdvig, ish_index, itog_indx= [], [], [] #Пустые массивчики для будущих штучек:)
    itog_stroka_shifr = ""
    for i in slovo_key: sdvig.append(alf.find(i)+1) #получается создали массив со всеми сдвигами
    #А и +1 ставим из-за того, что при букве A берет 0, значит считает не сдвиг, а индекс, значит плюсуем единицу
    sdvig *= 1000 #ну а вдруг слово юзера будет большим(если очень большим, то добавить пару ноликов еще можно):) что-то более умное придумывать не хочу:)))
    for i in slovo_for_shifr: ish_index.append(alf.find(i)) #создали массив со всеми исхожными индексами
    for i in range(len(ish_index)): itog_indx.append(ish_index[i] + sdvig[i])#нашли итоговый сдвиг для каждой буквы
    for i in itog_indx: itog_stroka_shifr += str(alf[i]) #усе, халява:)
    return itog_stroka_shifr
 #лично я считаю код элегантным и простым:) и самое главное - думать много не надо:)

def deshifr(slovo_key): #вот прям один в один как прошлое, только в формировании itog_indx "-" вместо "+"
    global alf
    slovo_for_deshifr = input("Введите слово, которое хотите дешифровать --> ").upper()
    sdvig, posle_shifr_index, itog_indx = [], [], []  # Пустые массивчики для будущих штучек:)
    itog_stroka_deshifr = ""
    for i in slovo_for_deshifr: posle_shifr_index.append(alf.find(i) + 1)
    for i in slovo_key: sdvig.append(alf.find(i) + 1)
    sdvig *= 1000
    for i in range(len(posle_shifr_index)): itog_indx.append((posle_shifr_index[i] - sdvig[i]) - 1)
    for i in itog_indx: itog_stroka_deshifr += str(alf[i])  # усе, халява:)
    return itog_stroka_deshifr

if choice == 1: #ну и вызовы тута всякие
    slovo_key = input("Введите ключевое слово --> ").upper()
    print(shifr(slovo_key))

if choice == 2: #ну и вызовы тута всякие
    slovo_key = input("Введите ключевое слово --> ").upper()
    print(deshifr(slovo_key))

