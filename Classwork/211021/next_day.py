day = int(input("Введите день "))
month = str(input("Введите месяц "))
year = int(input("Введите год "))

m = str(day) + month
if m == "31декабря":
    print("1 января" + " " + str(year + 1))
elif m == "31января":
    print("1 февраля" + " " + str(year))
elif m == "28февраля":
    print("1 марта" + " " + str(year))
elif m == "31марта":
    print("1апреля" + " " + str(year))
elif m == "30 апреля":
    print("1 мая" + " " + str(year))
elif m == "31мая":
    print("1 июня" + " " + str(year))
elif m == "30июня":
    print("1 июля" + " " + str(year))
elif m == "31июля":
    print("1 августа" + " " + str(year))
elif m == "31августа":
    print("1 сентября" + " " + str(year))
elif m == "30сентября":
    print("1 октября" + " " + str(year))
elif m == "31октября":
    print("1 ноября" + " " + str(year))
elif m == "30ноября":
    print("1 декабря" + " " + str(year))
else:
    print(str(day + 1) + " " + str(month) + " " + str(year))