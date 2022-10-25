alpha = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
beta = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
print('Введите шаг шифровки')
n = int(input())
if n>33 or n<0:
    print("Внимание, при таком шаге брутфорс выведет неверный шаг")
print('Введите сообщение для шифровки')
s = input()
res = ''
for i in s:
    if i==i.upper():
        res += alpha[(alpha.index(i) + n) % len(alpha)]
    else:
        res += beta[(beta.index(i) + n) % len(beta)]
print('зашифрованное сообщение:',res)
print('Введите шаг дешифровки')
n = int(input())
de=''
for i in res:
    if i==i.upper():
        de += alpha[(alpha.index(i) - n) % len(alpha)]
    else:
        de += beta[(beta.index(i) - n) % len(beta)]
print('расшифрованние сообщение:',de)
brut=''
for i in range (33):
    for j in res:
        if j == j.upper():
            brut += alpha[(alpha.index(j) + i) % len(alpha)]
        else:
            brut += beta[(beta.index(j) + i) % len(beta)]
    if brut==s:
        print('brutforce шаг:',33-i)
        print('brutforce:', brut)
    brut=''