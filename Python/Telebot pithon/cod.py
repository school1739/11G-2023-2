import telebot
from telebot import types

bot = telebot.TeleBot("5857977234:AAFd_270MScAQKKLiT6rEJU9yDztlrJK7m0")

@bot.message_handler(commands=['start'])
def url(message):
    markup=types.InlineKeyboardMarkup()
    btn1=types.InlineKeyboardButton(text='На сайт', url='https://педобраз.рф')
    markup.add(btn1)
    bot.send_message(message.from_user.id, "Нажми на кнопку, попадешь на сайт!", reply_markup=markup)