a = int(input("Литров:"))
b = int(input("Количество бутылок:"))
if a <= 1:
    print(b*0.1 , "₽")
else:
    print(b*0.25 , "₽")