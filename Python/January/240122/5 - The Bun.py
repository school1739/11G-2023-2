### Задание №5 "The Bun"
##
#
# функция для выводы песни
def bun_song(animal):
   print("Я Колобок, Колобок!")
   print("Я по коробу скребен,")
   print("По сусеку метен,")
   print("На сметане мешон,")
   print("Да в масле пряжон,")
   print("На окошке стужон;")
   print("Я от дедушки ушел,")
   print("Я от бабушки ушел,")
   for k in s_s:
      print(k)
   print("И от тебя, " + animal + ", убегу!")
   s_s.append("Я от " + animal + " ушел,")


s_s = []
a = ["заяцa", "лисы", 'волка','медведя']
for animal in a:  # вывод  песни
   bun_song(animal)

# OK