"""Интернет-магазин предоставляет услугу экспресс-доставки для части
своих товаров по цене $10,95 за первый товар в заказе и $2,95 – за все
последующие. Напишите функцию, принимающую в качестве единствен-
ного параметра количество товаров в заказе и возвращающую общую
сумму доставки. В основной программе должны производиться запрос
количества позиций в заказе у пользователя, и отображаться на экране
сумма доставки (сумму перевести в рубли по курсу $1 = 75₽."""
def dil(z):
    z = z - 1
    print("Сумма доставки: " + str((10.95 + (2.95 * z)) * 75))
dil(int(input("Введите количество заказов: ")))

# +-OK. Интересно, а где такую монету найти?
# Сумма доставки: 3476.2500000000005