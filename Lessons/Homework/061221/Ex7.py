import random # подключаем библиотеку random
a=''
i=0
max=0
while a !=100: # используем цикл while
   a=random.randint(1,100)
   if a>max:  # присваиваем  максимальное значение
       max=a
       i+=1
       print(">",a,"<== Обновление")
   else:
       print(">",a)
print('. . .')
print('максимальное значение в ряду:',max)
print('количество смен максимального значения:',i)