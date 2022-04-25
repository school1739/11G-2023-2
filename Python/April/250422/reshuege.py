# count=1
# max_count=1
# with open("zadanie24_2.txt", 'r') as file:
#     text=file.read()
#     for l in range(len(text)-1):
#         if text[l]=="L" and text[l]==text[l+1]:
#             count+=1
#             max_count=max(max_count, count)
#         else:
#             count=1
#     print(max_count)

with open('27886.txt', 'r') as file:
    lines=file.readlines()
    first_line=lines.pop(0).split()
    disk_size=int(first_line[0])
    user_count=int(first_line[1])
    lines=[int(1) for i in lines]
    lines.sort()
    backup_size=0
    backup_count=0
    max_line=0

    for line in lines:
        if backup_size+line<=disk_size:
            backup_size+=line
            backup_count+=1
            max_line=line
            print(line)
    for line in lines:
        if (backup_size-max_line)+line<=disk_size:
            big_line=line
    print(backup_count, big_line)

