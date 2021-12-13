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

lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
# или проще (/сложнее ?)
lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')

# Вывести стоимость каждого вида товара на складе:
# один раз распечать сколько всего столов и их общая стоимость,
# один раз распечать сколько всего стульев и их общая стоимость,
#   и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# TODO здесь ваш код

# СТОЛЫ
# Создание пустых переменных для последующего сложения
table_cost = 0
table_kol = 0
# Цикл, который повторяется по кол-ву элементов в списке, коорый соответствует ключу словаря
for i in range(len(store[goods["Стол"]])):
    # Счёт кол-ва
    table_kol += store[goods["Стол"]][i]['quantity']
    # Счёт стоимости
    table_cost += store[goods["Стол"]][i]['quantity'] * store[goods["Стол"]][i]['price']
print(f"Стол - {table_kol} шт, стоимость {table_cost} руб")

# ДИВАНЫ
# Создание пустых переменных для последующего сложения
sofa_cost = 0
sofa_kol = 0
# Цикл, который повторяется по кол-ву элементов в списке, коорый соответствует ключу словаря
for i in range(len(store[goods["Диван"]])):
    # Счёт кол-ва
    sofa_kol += store[goods["Диван"]][i]['quantity']
    # Счёт стоимости
    sofa_cost += store[goods["Диван"]][i]['quantity'] * store[goods["Диван"]][i]['price']
print(f"Диван - {sofa_kol} шт, стоимость {sofa_cost} руб")

# СТУЛЬЯ
# Создание пустых переменных для последующего сложения
chair_cost = 0
chair_kol = 0
# Цикл, который повторяется по кол-ву элементов в списке, коорый соответствует ключу словаря
for i in range(len(store[goods["Стул"]])):
    # Счёт кол-ва
    chair_kol += store[goods["Стул"]][i]['quantity']
    # Счёт стоимости
    chair_cost += store[goods["Стул"]][i]['quantity'] * store[goods["Стул"]][i]['price']
print(f"Стул - {chair_kol} шт, стоимость {chair_cost} руб")