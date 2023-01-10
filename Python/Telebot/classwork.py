import telebot
from telebot import types

bot=telebot.TeleBot("5971022632:AAERvUNF3X7JvzqIbEcMGaVkcaj2almTEsA")


"""bot = telebot.TeleBot('5971022632:AAERvUNF3X7JvzqIbEcMGaVkcaj2almTEsA')
@bot.message_handler(commands=['start'])
def url(message):
    markup=types.InlineKeyboardMarkup()
    btn1=types.InlineKeyboardButton(text="На сайт", url="https://педобраз.рф")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "Нажми на кнопку", reply_markup=markup)"""