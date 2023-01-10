import telebot
from telebot import types

bot = telebot.TeleBot(token='5889249524:AAHBfPSZWsPe9vygYzl4EqMp3WuE3cYG-Jc')


@bot.message_handler(commands=['start'])
def url(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="На сайт", url="https://yotube.com")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "НАЖИМАЙ", reply_markup=markup)
bot.infinity_polling()