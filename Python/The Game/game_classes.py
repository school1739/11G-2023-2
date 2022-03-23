import random

#Ну если честно, то очень мало чего понял:(
#бред тут и с рандомом, и вообще со всем, понимаешь, что в одном классе надо заглобалить переменную, а она в другом совсем классе
#и сделать это не получается... функциями гораздо проще:((
#Пушу, чтобы хотя бы 2 не было, а списывать как-то не интересно)

range_numbers = [-1000, 1000]


probability_cheat_1 = 0
probability_cheat_2 = 0
class cheat:
    def cheats(self, probabilty_cheat, amound_fails):
        cheat = False
        probability = random.randint(0, 100)
        self.probabilty = probability
        if self.probabilty <= probabilty_cheat and amound_fails >= 3:
            cheat = True
        return cheat
ch = cheat()

class player_1:
    def start_1(self, fails1_in_a_row):
        global probability_cheat_1
        global ch
        global range_numbers
        num1 = random.randint(*range_numbers)

        # Повышение вероятности чита после 3 проигрышей подряд
        if fails1_in_a_row == 3:
            probability_cheat_1 += 5
        # Активированность чита
        if ch.cheats(probability_cheat_1, fails1_in_a_row) is True:
            num1 += 1000
        # print(probabilty_cheat1)

        return num1
pl_1 = player_1()
class player_2:
    def start_2(self, fails2_in_a_row):

        global probability_cheat_2
        global range_numbers
        global ch
        num2 = random.randint(*range_numbers)
        # Повышение вероятности чита после 3 проигрышей подряд
        if fails2_in_a_row == 3:
            probability_cheat_2 += 5
        # Активированность чита
        if ch.cheats(probability_cheat_2, fails2_in_a_row) is True:
            num2 += 1000
        # print(probabilty_cheat2)
        return num2

pl_2 = player_2()
score_1 = 0
score_2 = 0

# Проигрыши и кол-во проигрышей подряд
fails1, fails1_in_a_row = 0, 0
fails2, fails2_in_a_row = 0, 0
class referee:
    def start_3(self):
        global pl_2
        global pl_1
        global fails1, fails1_in_a_row
        global fails2, fails2_in_a_row
        global score_1, score_2

        num_1 = pl_1.start_1(fails1_in_a_row)
        num_2 = pl_2.start_2(fails2_in_a_row)

        if num_1 == num_2:
            score_1 += 1
            score_2 += 1
            fails1_in_a_row, fails2_in_a_row = 0, 0
            print("Ничья")
        elif num_1 > num_2:
            score_1 -= 1
            score_2 += 1
            fails1 += 1
            fails1_in_a_row += 1
            fails2_in_a_row = 0
            print("Второй выиграл")

        elif num_1 < num_2:
            score_1 += 1
            score_2 -= 1
            fails2 += 1
            fails1_in_a_row = 0
            fails2_in_a_row += 1
            return ("Первый выиграл")

ref = referee()
# Раунды
for i in range(10000):
    ref.start_3()
    if score_1 == 50:
        print(f'Первый победил в игре')
        break
    elif score_2 == 50:
        print(f'Второй победил в игре')
        break
if score_1 < 50 and score_2 < 50:
    print(f'Никто не дошел до победого счета')