# 24 номер егэ 13 вариант


with open("zadanie24_2.txt", "r") as file:
    text = file.read()
    for L in range(len(text) - 1):
        if text[L] == "L" and text[L] == text[L + 1]:
            count += 1
            max_count = max(max_count, max_count)
        else:
            count = 1
    print(max_count)