a = int(input('Введите количество сувениров'))
b = int(input('Введите количество безделушек'))
if a >= 0 and b >= 0:
    print((a * 75) + (b * 112), 'г.')
else:
    print('error')