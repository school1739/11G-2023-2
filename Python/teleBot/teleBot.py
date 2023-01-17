import telebot
from telebot import types

bot = telebot.Telebot("5829625388:AAHPfkoEGOh1DG-Gpw-s6Qtu7cUh1buGUt0")

@bot.message_handler(commands=['start'])
def url(message):
    markup=types.InlineKeyboardMarkup()
    btn1=types.InlineKeyboardButton(text='На сайт', url='https://педобраз.рф')
    markup.add(btn1)
    bot.send_message(message.from_user.id, "Нажми на кнопку, попадешь на сайт!", reply_markup=markup)

@bot.message_handler(content_types = ["text"])
def get_text_message(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, человек")
    if message.text == "На сайт":
        bot.send_message(message.from_user.id, "https://педобраз.рф")
    if message.text == "help":
        bot.send_message(message.from_user.id, "Нажми на кнопку и получишь результат")
    if message.text == "/help":
        bot.send_message(message.from_user.id, "Это кнопка хелпы")
