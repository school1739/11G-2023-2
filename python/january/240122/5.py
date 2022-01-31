def ex(an):
    print("Я колобок колобок")
    print("Я от бабушки ушел")
    print("Я от дедушки ушел")
    for i in l:
        print(i)
    print("И от тебя " + str(an) + " убегу")
    l.append("Я от " + str(an) + " Ушел")
    print("               ")
l = []
an = ["Волк", "Лиса", "Другое существо"]
for q in an:
    ex(q)