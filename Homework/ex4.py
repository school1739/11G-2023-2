start_deposit = int(input())
def var_1():
    global start_deposit
    year_1 = start_deposit * 1.04
    year_2 = year_1 * 1.04
    year_3 = year_2 * 1.04
    print(("{0:.2f}".format(year_1)), ("{0:.2f}".format(year_2)), ("{0:.2f}".format(year_3)))
var_1()