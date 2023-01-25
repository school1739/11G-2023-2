import telebot
from telebot import types

bot = telebot.TeleBot(token='5889249524:AAHBfPSZWsPe9vygYzl4EqMp3WuE3cYG-Jc')


@bot.message_handler(commands=['start'])
def url(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    btn1 = types.KeyboardButton('Привет')
    btn2 = types.KeyboardButton('На сайт')
    btn3 = types.KeyboardButton('gif')
    btn4 = types.KeyboardButton('png')
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.from_user.id, "нажми", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_message(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет!")
    if message.text == "На сайт":
        bot.send_message(message.from_user.id, "https://xn--80abidn3bem.xn--p1ai/")
    if message.text == "gif":
        bot.send_message(message.from_user.id, "https://media2.giphy.com/media/QxNWNSdkzxtIrOTsPn/giphy.webp")
    if message.text == "png":
        bot.send_message(message.from_user.id, "https://fikiwiki.com/uploads/posts/2022-02/1645003687_1-fikiwiki-com-p-kartinki-fantasticheskie-miri-1.jpg")

bot.polling()