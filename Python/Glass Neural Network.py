### Нейросеть из стаканов
##
#
import random

count = 0 # счётчик побед компьютера
glass2 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
glass3 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
glass4 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
glass5 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
glass6 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
glass7 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
glass8 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
glass9 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
glass10 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
glass11 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
Winner=""

while count <= 4: # повторяем пока еомпьютер не победит 5 раз
    print("На столе 11 палочек")
    if Winner != "computer": # проходимся по всем стаканам, попутно выводя результат
        sticks = 11
        step1 = random.choice(glass11)
        print("Компьютер забрал", step1, "палочек") # в целом, из принта видно, что мы делаем
        if step1 == 1:
            sticks -= 1
            number0 = 1
        else:
            sticks -= 2
            number0 = 2
        print("Осталось", sticks, "палочек")
        player = random.randint(1, 2)
        print("Игрок забрал", player, "палочек")
        if player == 1:
            sticks -= 1
        else:
            sticks -= 2
        print("Осталось",sticks, "палочек")
        if sticks == 9:                         # рассматриваем все возможные вариатны
            step2 = random.choice(glass9)
            print("Компьютер забрал", step2, "палочек")
            number4 = ""
            number3 = ""
            if step2 == 1:
                sticks -= 1
                number2 = 1
            else:
                sticks -= 2
                number2 = 2
            print("Осталось",sticks, "палочек")
        elif sticks == 8:                            # это наверняка можно было слелать намного проще
            number2 = ""
            number4 = ""
            step2 = random.choice(glass8)
            print("Компьютер забрал", step2, "палочек")
            if step2 == 1:
                sticks -= 1
                number3 = 1
            else:
                sticks -= 2
                number3 = 2
            print("Осталось", sticks, "палочек")
        elif sticks == 7:                              # но ничего другого мне в голову не пришло
            number2 = ""
            number3 = ""
            step2 = random.choice(glass7)
            print("Компьютер забрал", step2, "палочек")
            if step2 == 1:
                sticks -= 1
                number4 = 1
            else:
                sticks -= 2
                number4 = 2
            print("Осталось", sticks, "палочек")
        player = random.randint(1, 2)
        print("Игрок забрал", player, "палочек")
        if player == 1:
            sticks -= 1
        else:
            sticks -= 2
        print("Осталось",sticks, "палочек")
        if sticks == 7:
            number5 = ""
            number6 = ""
            number8 = ""
            step3 = random.choice(glass7)
            print("Компьютер забрал", step3, "палочек")
            if step3 == 1:
                sticks -= 1
                number4 = 1
            else:
                sticks -= 2
                number4 = 2
            print("Осталось", sticks, "палочек")
        elif sticks == 6:
            number6 = ""
            number8 = ""
            number4 = ""
            step3 = random.choice(glass6)
            print("Компьютер забрал", step3, "палочек")
            if step3 == 1:
                sticks -= 1
                number5 = 1
            else:
                sticks -= 2
                number5 = 2
            print("Осталось", sticks, "палочек")
        elif sticks == 5:
            number5 = ""
            number4 = ""
            number8 = ""
            step3 = random.choice(glass5)
            print("Компьютер забрал", step3, "палочек")
            if step3 == 1:
                sticks -= 1
                number6 = 1
            else:
                sticks -= 2
                number6 = 2
            print("Осталось", sticks, "палочек")
        elif sticks == 4:
            step3 = random.choice(glass4)
            print("Компьютер забрал", step3, "палочек")
            number5 = ""               # О, это я таким образом нашла способ убирать числа только из нужного стаканчика
            number6 = ""
            number8 = ""
            number4 = ""
            number9 = ""
            if step3 == 1:
                sticks -= 1
                number7 = 1
            else:
                sticks -= 2
                number7 = 2
            print("Осталось", sticks, "палочек")
        elif sticks == 3:
            step3 = random.choice(glass3)
            print("Компьютер забрал", step3, "палочек")
            number5 = ""
            number4 = ""
            number6 = ""            # опять же, это наверняка можно было сделать проще
            number7 = ""
            number9 = ""
            if step3 == 1:
                sticks -= 1
                number8 = 1
            else:
                sticks -= 2
                number8 = 2
                Winner = "computer"
            print("Осталось", sticks, "палочек")
        player = random.randint(1, 2)
        print("Игрок забрал", player, "палочек")
        if player == 1:
            sticks -= 1
            if sticks == 1:
                Winner = "player"
        else:
            sticks -= 2
            if sticks == 1:
                Winner = "player"
            elif sticks == 0:
                Winner = "player"
        print("Осталось",sticks, "палочек")
        if sticks == 5:
            step4 = random.choice(glass5)
            print("Компьютер забрал", step4, "палочек")
            number9 = ""
            number7 = ""
            if step4 == 1:
                sticks -= 1
                number6 = 1
            else:
                sticks -= 2
                number6 = 2
            print("Осталось", sticks, "палочек")
        elif sticks == 4:
            step4 = random.choice(glass4)
            print("Компьютер забрал", step4, "палочек")
            number9 = ""
            if step4 == 1:
                sticks -= 1
                number7 = 1
            else:
                sticks -= 2
                number7 = 2
            print("Осталось", sticks, "палочек")
        elif sticks == 3:
            number7 = ""
            number9 = ""
            step4 = random.choice(glass3)
            print("Компьютер забрал", step4, "палочек")
            if step4 == 1:
                sticks -= 1
                number8 = 1
            else:
                sticks -= 2
                number8 = 2
                Winner = "computer"
            print("Осталось", sticks, "палочек")
        elif sticks == 2:
            step4 = random.choice(glass2)
            print("Компьютер забрал", step4, "палочек")
            number7 = ""
            if step4 == 1:
                sticks -= 1
                number9 = 1
                Winner = "computer"
            else:
                sticks -= 2
                number9 = 2
                Winner = "player"
            print("Осталось", sticks, "палочек")
        if sticks>=2:
            player = random.randint(1, 2)
            print("Игрок забрал", player, "палочек")
            if player == 1:
                sticks -= 1
                if sticks == 1:
                    Winner = "player"
            else:
                sticks -= 2
                if sticks == 1:
                    Winner = "player"
                elif sticks == 0:
                    Winner = "computer"
            print("Осталось",sticks, "палочек")
        if sticks == 3:
            step5 = random.choice(glass3)
            print("Компьютер забрал", step5, "палочек")
            number9 = ""
            if step5 == 1:
                sticks -= 1
                number8 = 1
            else:
                sticks -= 2
                number8 = 2
                Winner = "computer"
            print("Осталось", sticks, "палочек")
        elif sticks == 2:
            step5 = random.choice(glass2)
            print("Компьютер забрал", step5, "палочек")
            if step5 == 1:
                sticks -= 1
                number9 = 1
                Winner = "computer"
            else:
                sticks -= 2
                number9 = 2
                Winner = "player"
            print("Осталось", sticks, "палочек")
        if sticks == 2:
            player = random.randint(1, 2)
            if player == 1:
                Winner = "player"
            else:
                Winner = "computer"
            print("Осталось", sticks, "палочек")
        if Winner == "computer": # мы наконец дошли до добавления или убирания чисел
            count += 1
            glass11.append(number0)
            if number2 == 1 or number2 == 2:
                glass9.append(number2)
            if number3 == 1 or number3 == 2:
                glass8.append(number3)
            if number4 == 1 or number4 == 2:
                glass7.append(number4)
            if number5 == 1 or number5 == 2:
                glass6.append(number5)
            if number6 == 1 or number6 == 2:
                glass5.append(number6)
            if number7 == 1 or number7 == 2:
                glass4.append(number7)
            if number8 == 1 or number8 == 2:
                glass3.append(number8)
            if number9 == 1 or number9 == 2:
                glass2.append(number9)
        else:
            count = 0
            if len(glass11) != 1:
                glass11.remove(number0)
            if number2 == 1 or number2 == 2:
                if len(glass9) != 1:
                    glass9.remove(number2)
            if number3 == 1 or number3 == 2:
                if len(glass8) != 1:
                    glass8.remove(number3)
            if number4 == 1 or number4 == 2:
                if len(glass7) != 1:
                    glass7.remove(number4)
            if number5 == 1 or number5 == 2:
                if len(glass6) != 1:
                    glass6.remove(number5)
            if number6 == 1 or number6 == 2:
                if len(glass5) != 1:
                    glass5.remove(number6)
            if number7 == 1 or number7 == 2:
                if len(glass4) != 1:
                    glass4.remove(number7)
            if number8 == 1 or number8 == 2:
                if len(glass3) != 1:
                    glass3.remove(number8)
            if number9 == 1 or number9 == 2:
                if len(glass2) != 1:
                    glass2.remove(number9)
    elif Winner!="player": # теперь, если первый будет ходит игрок
        sticks=11
        player=random.randint(1,2)
        print("Игрок забрал", player, "палочек")
        if player==1:
            sticks-=1
        else:
            sticks-=2
        print("Осталось",sticks, "палочек")
        if sticks==10:
            step1=random.choice(glass10)
            print("Компьютер забрал", step1, "палочек")  # тут, вобщем-то, всё тоже самое
            number2=""
            if step1==1:
                sticks-=1
                number1=1
            else:
                sticks-=2
                number1=2
            print("Осталось", sticks, "палочек")
        elif sticks==9:
            step1=random.choice(glass9)
            print("Компьютер забрал", step1, "палочек")
            number1= ""
            if step1==1:
                sticks-=1
                number2=1
            else:
                sticks-=2
                number2=2
            print("Осталось", sticks, "палочек")
        player=random.randint(1,2)
        print("Игрок забрал", player, "палочек")
        if player==1:
            sticks-=1
        else:
            sticks-=2
        print("Осталось",sticks, "палочек")
        if sticks==8:
            step2=random.choice(glass8)
            print("Компьютер забрал", step2, "палочек")
            number4=""
            number5=""
            number6=""
            if step2==1:
                sticks-=1
                number3=1
            else:
                sticks-=2
                number3=2
            print("Осталось", sticks, "палочек")
        elif sticks==7:
            step2=random.choice(glass7)
            print("Компьютер забрал", step2, "палочек")
            number3=""
            number5=""
            number6=""
            if step2==1:
                sticks-=1
                number4=1
            else:
                sticks-=2
                number4=2
            print("Осталось", sticks, "палочек")
        elif sticks==6:
            step2=random.choice(glass6)
            print("Компьютер забрал", step2, "палочек")
            number3=""
            number4=""
            number6=""
            if step2==1:
                sticks-=1
                number5=1
            else:
                sticks-=2
                number5=2
            print("Осталось", sticks, "палочек")
        elif sticks==5:
            number3=""
            number4=""
            number5=""
            step2=random.choice(glass5)
            print("Компьютер забрал", step2, "палочек")
            if step2==1:
                sticks-=1
                number6=1
            else:
                sticks-=2
                number6=2
            print("Осталось", sticks, "палочек")
        player=random.randint(1,2)
        print("Игрок забрал", player, "палочек")
        if player==1:
            sticks-=1
        else:
            sticks-=2
            if sticks==1:
                Winner="player"
            print("Осталось", sticks, "палочек")
        if sticks==6:
            step3=random.choice(glass6)
            print("Компьютер забрал", step3, "палочек")
            number6=""
            number7=""
            number8=""
            number9=""
            if step3==1:
                sticks-=1
                number5=1
            else:
                sticks-=2
                number5=2
            print("Осталось", sticks, "палочек")
        elif sticks==5:
            step3=random.choice(glass5)
            print("Компьютер забрал", step3, "палочек")
            number5=""
            number7=""
            number8=""
            number9=""
            if step3==1:
                sticks-=1
                number6=1
            else:
                sticks-=2
                number6=2
            print("Осталось", sticks, "палочек")
        elif sticks==4:
            step3=random.choice(glass4)
            print("Компьютер забрал", step3, "палочек")
            number6=""
            number5=""
            number8=""
            number9=""
            if step3==1:
                sticks-=1
                number7=1
            else:
                sticks-=2
                number7=2
            print("Осталось", sticks, "палочек")
        elif sticks==3:
            step3=random.choice(glass3)
            print("Компьютер забрал", step3, "палочек")
            number6=""
            number7=""
            number5=""
            number9=""
            if step3==1:
                sticks-=1
                number8=1
            else:
                sticks-=2
                number8=2
                Winner="computer"
            print("Осталось", sticks, "палочек")
        elif sticks==2:
            step3=random.choice(glass2)
            print("Компьютер забрал", step3, "палочек")
            number6=""
            number7=""
            number8=""
            number5=""
            if step3==1:
                sticks-=1
                number9=1
                Winner="computer"
            else:
                sticks-=2
                number9=2
                Winner="player"
            print("Осталось", sticks, "палочек")
        if sticks>=2:
            player=random.randint(1,2)
            print("Игрок забрал", player, "палочек")
            if player==1:
                sticks-=1
                if sticks==1:
                    Winner="player"
            else:
                sticks-=2
                if sticks==1:
                    Winner="player"
                elif sticks==0:
                    Winner="computer"
            print("Осталось",sticks, "палочек")
        if sticks==4:
            step4=random.choice(glass4)
            print("Компьютер забрал", step4, "палочек")
            number8=""
            number9=""
            if step4==1:
                sticks-=1
                number7=1
            else:
                sticks-=2
                number7=2
            print("Осталось", sticks, "палочек")
        elif sticks==3:
            step4=random.choice(glass3)
            print("Компьютер забрал", step4, "палочек")
            number7=""
            number9=""
            if step4==1:
                sticks-=1
                number8=1
            else:
                sticks-=2
                number8=2
                Winner="computer"
            print("Осталось", sticks, "палочек")
        elif sticks==2:
            step4=random.choice(glass2)
            print("Компьютер забрал", step4, "палочек")
            number8=""
            number7=""
            if step4==1:
                sticks-=1
                number9=1
                Winner="computer"
            else:
                sticks-=2
                number9=2
                Winner="player"
            print("Осталось", sticks, "палочек")
        if sticks>=2:
            player=random.randint(1,2)
            print("Игрок забрал", player, "палочек")
            if player==1:
                sticks-=1
                if sticks==1:
                    Winner="player"
            else:
                sticks-=2
                if sticks==1:
                    Winner="player"
                elif sticks==0:
                    Winner="computer"
            print("Осталось", sticks, "палочек")
        if sticks==2:
            step5=random.choice(glass2)
            print("Компьютер забрал", step5, "палочек")
            if step5==1:
                sticks-=1
                number9=1
                Winner="computer"
            else:
                sticks-=2
                number9=2
                Winner="player"
            print("Осталось", sticks, "палочек")
        if Winner == "computer":
            count += 1
            if number1==1 or number1==2:
                glass10.append(number1)
            if number2 == 1 or number2 == 2:
                glass9.append(number2)
            if number3 == 1 or number3 == 2:
                glass8.append(number3)
            if number4 == 1 or number4 == 2:
                glass7.append(number4)
            if number5 == 1 or number5 == 2:
                glass6.append(number5)
            if number6 == 1 or number6 == 2:
                glass5.append(number6)
            if number7 == 1 or number7 == 2:
                glass4.append(number7)
            if number8 == 1 or number8 == 2:
                glass3.append(number8)
            if number9 == 1 or number9 == 2:
                glass2.append(number9)
        else:
            count = 0
            if number1==1 or number1==2:
                if len(glass10) != 1:
                    glass10.remove(number1)
            if number2 == 1 or number2 == 2:
                if len(glass9) != 1:
                    glass9.remove(number2)
            if number3 == 1 or number3 == 2:
                if len(glass8) != 1:
                    glass8.remove(number3)
            if number4 == 1 or number4 == 2:
                if len(glass7) != 1:
                    glass7.remove(number4)
            if number5 == 1 or number5 == 2:
                if len(glass6) != 1:
                    glass6.remove(number5)
            if number6 == 1 or number6 == 2:
                if len(glass5) != 1:
                    glass5.remove(number6)
            if number7 == 1 or number7 == 2:
                if len(glass4) != 1:
                    glass4.remove(number7)
            if number8 == 1 or number8 == 2:
                if len(glass3) != 1:
                    glass3.remove(number8)
            if number9 == 1 or number9 == 2:
                if len(glass2) != 1:
                    glass2.remove(number9)
    print("Победил",Winner) # ну, и кто победил в итоге
# вроде как работает :)