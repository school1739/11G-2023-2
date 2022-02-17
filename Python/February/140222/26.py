from math import fmod

with open('26.txt') as file:
    list_of_numbers = list(map(int, file.read().split()))
    N = list_of_numbers.pop(0)
count = 0
max_avg = 0
for number in list_of_numbers:
    if fmod(number, 2) == 1:
        for number_2 in list_of_numbers:
            avg_of_nums = (number + number_2) / 2
            if avg_of_nums in list_of_numbers:
                count += 1
                if max_avg < avg_of_nums:
                    max_avg = avg_of_nums
print(count, max_avg)

