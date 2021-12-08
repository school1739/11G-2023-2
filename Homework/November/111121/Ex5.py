

byte = input()
if len(byte)==8:
    while byte!='':
        if byte.count('1')%2==0:
            print(byte + '1')
        else:
            print(byte+'0')
        byte=input()
else:
    print('Надо 8 знаков')