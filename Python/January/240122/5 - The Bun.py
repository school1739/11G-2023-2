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
    for string in songs_strings:
        print(string)
    print("И от тебя, " + animal + ", убегу!")
    songs_strings.append("Я от " + animal + " ушел,")


songs_strings = []
animals = ["заяцa", "лисы", 'волка','медведя']
for animal in animals:  # вывод  песни
    bun_song(animal)

# OK