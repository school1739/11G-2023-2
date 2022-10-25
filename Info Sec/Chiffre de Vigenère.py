alpha = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
beta = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
print('сообщение для шифровки')
a = input()
print('кодовое слово')
b = input()
c = ''
d = []
for i in range(len(b)):
    if b[i].upper() == b[i]:
        d.append(alpha.index(b[i]))
    else:
        d.append(beta.index(b[i]))
for i in range(len(a)):
    if a[i].upper() == a[i] and a[i] != ' ':
        c = c + alpha[alpha.index(a[i]) + d[i % len(d)]]
    elif a[i] == ' ':
        c = c + ' '
    else:
        c = c + beta[beta.index(a[i]) + d[i % len(d)]]
print('шифрованное слово:',c)
print('сообщение для дешифровки')
a = input()
print('кодовое слово для дешифровки')
b = input()
c = ''
d = []
for i in range(len(b)):
    if b[i].upper() == b[i]:
        d.append(alpha.index(b[i]))
    else:
        d.append(beta.index(b[i]))
for i in range(len(a)):
    if a[i].upper() == a[i] and a[i] != ' ':
        c = c + alpha[alpha.index(a[i]) - d[i % len(d)]]
    elif a[i] == ' ':
        c = c + ' '
    else:
        c = c + beta[beta.index(a[i]) - d[i % len(d)]]
print('дешифрованное сообщение:',c)
