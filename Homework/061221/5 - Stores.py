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

# lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
# # или проще (/сложнее ?)
# lamp_code = goods['Лампа']
# lamps_item = store[lamp_code][0]
# lamps_quantity = lamps_item['quantity']
# lamps_price = lamps_item['price']
# lamps_cost = lamps_quantity * lamps_price
# print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')

# Вывести стоимость каждого вида товара на складе:
# один раз распечать сколько всего столов и их общая стоимость,
# один раз распечать сколько всего стульев и их общая стоимость,
#   и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# Задаём переменные для общего количества отдельного товара,
# кол-ва по определённой цене
# и общей стоимости каждого вида товара
quantity_product = 0
quantity_one_cost = 0
cost = 0
# Проходим циклами по элементам словарей
for product_name in goods:
    for item in store[goods[product_name]]:
        # Находим количество товара по определенной цене
        quantity_one_cost = item['quantity']
        # Суммируем в количество по отдельному товару
        quantity_product += quantity_one_cost
        # Находим стоимость имеющегося кол-ва товара по каждой цене
        # и суммируем в общую стоимость одного вида товара
        cost += quantity_one_cost * item['price']
    # Выводим на печать результаты
    print(f'{product_name} - {quantity_product} шт, стоимость {cost} руб')
    # Обнуляем переменные для подсчёта по следующему товару
    quantity_product = 0
    cost = 0
