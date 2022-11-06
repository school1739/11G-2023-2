#Ну штош, поехали:)
import random
from math import log
print("Можете ввести свои два числа p и q - 1 в консоль, или можете воспользоваться рандомом - 2 в консоль --> ")
if int(input()) == 1:
    p = int(input("Введите число q --> "))
    q = int(input("Введите число p --> "))
else:
    print("Окей, рандом так рандом")
    p = random.randint(2**7, 2**12) #ну чет считает миллиард лет, если поставить от 2**128 до 2**140
    q = random.randint(2**7, 2**12)#Давайте снизим планочку (И они не простые)
#Числа получили, теперь вычисляем ключи

n = p * q #"Модуль"
func_ailer = (p - 1)*(q - 1) #Функция Эйлера

#Вычисляем все делители этой функции
spisok_s_delitel = []
for i in range(2, func_ailer):
    if func_ailer % i == 0:
        spisok_s_delitel.append(i)

#теперь находим то самое число e, которое не имеет общих делителей с числом эйлера
for e in range(2, func_ailer):
    fl = True
    for delit in spisok_s_delitel:
        if e % delit == 0:
            fl = False
            break
    if fl:
        chislo_e = e
        break

for d in range(2, 2*1000):  #Нашли число d
    if (chislo_e * d - 1) % func_ailer:
        chislo_d = d
        break
#Ура, нашли все нужные эти хрени:) --> записываем все это в файл
#Записываем числа e и n в открытый ключ
file_with_keys_e_n = open("file_with_keys_e_n", "w+")
file_with_keys_e_n.write("e - " + str(chislo_e))
file_with_keys_e_n.write("      ")           #Не ну и долго же я с этим возился
                                            #Че-то и с кодировкой были проблемы и с самим кодом, но вроде норм
file_with_keys_e_n.write("n - " + str(n))
file_with_keys_e_n.close()


#А числа d и n в закрытый ключ
file_with_keys_e_n = open("file_with_keys_d_n", "w+")
file_with_keys_e_n.write("d - " + str(chislo_d))
file_with_keys_e_n.write("      ")           #Не ну и долго же я с этим возился
                                            #Че-то и с кодировкой были проблемы и с самим кодом, но вроде норм
file_with_keys_e_n.write("n - " + str(n))
file_with_keys_e_n.close()
#Первый пукт первого пункта сделали!!!!

#делаем второй пункт первого пункта!!!!!!!!!!!


#Шифруемый текст Т, все как в инструкции
file_with_shifr_text = open("file_with_shifr_text", "w+")
file_with_shifr_text.write(input("Введите текст для шифрования --> "))
file_with_shifr_text.close()
#<-----------ШИФРОВКА---------> #а может и нет, ибо после прочтения и понимания того, что ничего не понятно, плохо стало
#Такс, ну предположим, что он разбивает свое сообщение на блоки длиной [log2 n] - 1 бит, ну ибо в противном случае че-то анрил получается
#Да и в противном случае вообще не вижу способа как это сделать:) так шо лучше хотя бы так

k = int(log(n, 2)) #Нашли k
bloki_c_i = [] #Ну куда эти блоки девать не было сказано:) Значит будем в список засовывать
for blok_m_i in range(0, 2**k - 1):  #Считаем эти блоки
    blok_c_i = (blok_m_i)**chislo_e % n
    dv_predstav_c_i = bin(blok_c_i)[2:]
    dv_predstav_c_i = "0"*(k-len(dv_predstav_c_i)) + dv_predstav_c_i
    bloki_c_i.append(dv_predstav_c_i)


#в процессе шифрования предусмотреть возможность просмотра и изменения шифруемого текста в шестнадцатеричном и символьном видe.....
#Ниче не понятно, так что да

#<---------ДЕШИФРОВКА------->
deshifr_m_i = [] #Сюда складываем все блоки m_i, которые дешифруем

for c_i in bloki_c_i:
    m_i = int(c_i)**chislo_d % n
    deshifr_m_i.append(m_i)


file_with_blocks_c_i = open("file_with_blocks_c_i", "w+")
for i in bloki_c_i:
    file_with_blocks_c_i.write(str(i))
    file_with_blocks_c_i.write(" ")
file_with_blocks_c_i.close()



file_with_blocks_m_i = open("file_with_blocks_m_i", "w+")
for i in deshifr_m_i:
    file_with_blocks_m_i.write(str(i))
    file_with_blocks_m_i.write(" ")
file_with_blocks_m_i.close()

#АММ, ну усе вроде как, данные в файле странные конечно, но я сделал все что мог:)
print("БИП БУМ ПАК")
print("Готово, можете проверить новые файлы:) --> они будут в папочке info sec") #Но перед каждым запуском их надо удалять, а то они не перезаписываются почему-то