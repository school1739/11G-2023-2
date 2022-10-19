alf = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
choice = int(input("Введите 1 или 2, 1 - шифрование, 2 - дешифрование"))

def shifr(slovo_key):
    global alf
    slovo_for_shifr = input("Введите слово, для шифрования:").upper()
    sdvig, ish_index, itog_indx= [], [], []
    itog_stroka_shifr = ""
    for i in slovo_key: sdvig.append(alf.find(i)+1)
    sdvig *= 1000
    for i in slovo_for_shifr: ish_index.append(alf.find(i))
    for i in range(len(ish_index)): itog_indx.append(ish_index[i] + sdvig[i])
    for i in itog_indx: itog_stroka_shifr += str(alf[i])
    return itog_stroka_shifr
def deshifr(slovo_key):
    global alf
    slovo_for_deshifr = input("Введите слово, для дешифрования:").upper()
    sdvig, posle_shifr_index, itog_indx = [], [], []
    itog_stroka_deshifr = ""
    for i in slovo_for_deshifr: posle_shifr_index.append(alf.find(i) + 1)
    for i in slovo_key: sdvig.append(alf.find(i) + 1)
    sdvig *= 1000
    for i in range(len(posle_shifr_index)): itog_indx.append((posle_shifr_index[i] - sdvig[i]) - 1)
    for i in itog_indx: itog_stroka_deshifr += str(alf[i])
    return itog_stroka_deshifr

if choice == 1:
    slovo_key = input("Введите ключевое слово:").upper()
    print(shifr(slovo_key))

if choice == 2:
    slovo_key = input("Введите ключевое слово:").upper()
    print(deshifr(slovo_key))

