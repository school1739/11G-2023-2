a, b = 179, 37
count=0
ostatok=a
while ostatok > b:
    ostatok = ostatok - b
    count += 1
print('Целочисленное деление', a, 'на', b, 'даёт', count)