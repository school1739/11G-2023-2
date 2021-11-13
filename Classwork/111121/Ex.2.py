### Задание 2. Никаких центов!
##
# Запрашиваем у пользователя цены
#
from math import *
c=input()
S=0
while c!='':
    S=S+c
    c=input()
    print(S)
    print((round(S/5.0)*5))
