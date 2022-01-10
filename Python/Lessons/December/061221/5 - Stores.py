# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп
sum_lampa = 0
sum_stol = 0
sum_divan = 0
sum_stul = 0
for i in range(1):
    lampa_amount = store[goods["Лампа"]][i]["quantity"]
    lampa_cost = lampa_amount * store[goods["Лампа"]][i]["price"]
    sum_lampa = sum_lampa + lampa_cost
for i in range(2):
    stol_amount = store[goods["Стол"]][i]["quantity"]
    stol_cost = stol_amount * store[goods["Стол"]][i]["price"]
    sum_stol = sum_stol + stol_cost
for i in range(2):
    divan_amount = store[goods["Диван"]][i]["quantity"]
    divan_cost = divan_amount * store[goods["Диван"]][i]["price"]
    sum_divan = sum_divan + divan_cost
for i in range(3):
    stul_amount = store[goods["Стул"]][i]["quantity"]
    stul_cost = stul_amount * store[goods["Стул"]][i]["price"]
    sum_stul  = sum_stul  + stul_cost

print('Лампа -', lampa_amount, 'шт, стоимость', sum_lampa, 'руб')
print('Стол -', stol_amount, 'шт, стоимость', sum_stol, 'руб')
print('Диван -', divan_amount, 'шт, стоимость', sum_divan, 'руб')
print('Стул -', stul_amount, 'шт, стоимость', sum_stul, 'руб')

# Evaluation: OK