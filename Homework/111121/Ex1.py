a = int(input())  # input a number

if a == 0:  # if the first number is 0 you will receive a error
    print('Error')

i = 0  # cycle counter
b = a

while a != 0:
    a = int(input())  # input a number
    b = b + a
    i += 1
    if a == 0:
        print(b / i)  # you get the average sum of numbers which you inputted earlier

# Evaluation: OK