file=open('24-1.txt')
split = file.readline()

count = 0
max = 0

for i in range(len(split)):
    if split[i]=='X' and split[i+1]=='Y' and split[i+2]=='Z' and current ==0:
        current=1
        count += 1
        if count > max:
            max = count
    elif split[i] == 'X':
        count = 0
    else:
        count = 0
        current = 0
print(max)
