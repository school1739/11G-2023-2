"""Предприятие производит закупку изделий A и B, на которую выделена определённая сумма денег.
У поставщика есть в наличии различные модификации этих изделий по различной цене.
При покупке необходимо руководствоваться следующими правилами:

1. Нужно купить как можно больше изделий, независимо от их типа и модификации.
2. Если можно разными способами купить максимальное количество изделий, нужно выбрать тот способ,
    при котором будет куплено как можно больше изделий B.
3. Если можно разными способами купить максимальное количество изделий с одинаковым количеством изделий B,
    нужно выбрать тот способ, при котором вся покупка будет дешевле.

Определите, сколько всего будет куплено изделий B и какая сумма останется неиспользованной.

Входные данные.

Первая строка входного файла содержит два целых числа: N — общее количество изделий у поставщика и M — сумма
выделенных на закупку денег (в рублях). Каждая из следующих N строк содержит целое число (цена изделия в рублях)
и символ (латинская буква A или B), определяющий тип изделия. Все данные в строках входного файла отделены одним пробелом.
В ответе запишите два целых числа: сначала количество закупленных изделий типа B, затем оставшуюся неиспользованной сумму денег.
Пример входного файла:

6 130
30 A
50 A
60 B
20 B
70 B
10 A

В данном случае можно купить не более 4 изделий, из них не более 2 изделий B.
Минимальная цена такой покупки 120 рублей (покупаем изделия 30A, 60B, 20B, 10A).
Останется 10 рублей. В ответе надо записать числа 2 и 10."""

# EGE 26


with open('26.txt', 'r') as file:  # open for reading

    lines = file.readlines()  # read file lines recording to the variable
    first_line = lines.pop(0).split()  # separate the first line

    products = int(first_line[0])  # find out the quantity of products
    first_money = int(first_line[1])  # find out the amount of money

    lines.sort()  # sort in ascending order

    products_counter = 0  # quantity of purchased products
    second_money = first_money  # checking the max product quantity

    # quantity of products: B and A
    B_counter = 0
    A_counter = 0

    # while the lists of products are empty
    B_products = []
    A_products = []

    # compose the lists of products
    for line in lines:

        if line[5] == "B":
            B_products.append(line[0:4])

        elif line[5] == "A":
            A_products.append(line[0:4])

    for line in lines:

        if second_money >= int(line[0:4]):  # check the amount of remaining money and the prices of products
            products_counter += 1  # increase the products quantity
            second_money -= int(line[0:4])  # subtract the product price

        else:
            break

    # look for a max quantity of products B which are available for buying
    for product in B_products:

        if first_money >= int(product):  # check the rest of money and the product price
            B_counter += 1  # increase the quantity of products B
            first_money -= int(product)  # subtract the product price

        else:
            break

    # while the quantity of products A and B are less than the general amount of products - add products A
    # then if money is over - exclude the most expensive product B
    while B_counter + A_counter < products_counter:

        if first_money >= int(A_products[A_counter]):
            first_money -= int(A_products[A_counter])
            A_counter += 1

        else:
            B_counter -= 1
            first_money += int(B_products[B_counter])

print(B_counter, first_money)  # display the quantity of products B and the rest of money
