"""Интернет-магазин предоставляет услугу экспресс-доставки для части
своих товаров по цене $10,95 за первый товар в заказе и $2,95 – за все
последующие. Напишите функцию, принимающую в качестве единствен-
ного параметра количество товаров в заказе и возвращающую общую
сумму доставки. В основной программе должны производиться запрос
количества позиций в заказе у пользователя, и отображаться на экране
сумма доставки (сумму перевести в рубли по курсу $1 = 75₽."""
def tovar(kol):
    sum = 10.95+(kol-1)*2.95
    kyrs = sum*75
    return(kyrs)
kol=int(input())
print(tovar(kol))

# +-OK. Same -- глупый пользователь ничего не понимает.