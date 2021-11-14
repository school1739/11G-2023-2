#Grach_Fe
user_minute = int(input("Введите количество израсходованных минут: "))
user_sms = int(input("Введите количество израсходованных смс: "))
cost_min = 0
cost_sms = 0

if user_minute > 50:
    cost_min = user_minute - 50
    cost_min = cost_min * 0.25
#Grach_Fe
if user_sms > 50:
    cost_sms = user_sms - 50
    cost_sms = cost_sms * 0.15

if user_sms > 50 and user_minute > 50:
    print("Сумма доп минут и смс: " + str(cost_min + cost_sms))

all_sum = 15 + 0.44 + cost_min + user_sms
#Grach_Fe
print("базовая сумма тарификации: {0:.2f}".format((15 + 0.44)*1.05))
print("Проц колл центрам: {0:.2f}".format(0.44))
print("Налог: {0:.2f}".format(all_sum * 1.05 - all_sum))
print("Вся сумма: {0:.2f}".format(all_sum * 1.05))
#Grach_Fe

# Evaluation: OK