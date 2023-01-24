import telebot
from telebot import types

bot = telebot.TeleBot("5829625388:AAHPfkoEGOh1DG-Gpw-s6Qtu7cUh1buGUt0")

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
    elif message.text == "На сайт":
        bot.send_message(message.from_user.id, "https://педобраз.рф")
    elif message.text == "help":
        bot.send_message(message.from_user.id, "Нажми на кнопку и получишь результат")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Это кнопка хелпы")
    elif message.text == "Пришли картинку":
        bot.send_photo(message.from_user.id, "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Sandkat1_%28Felis_margarita%29.jpg/800px-Sandkat1_%28Felis_margarita%29.jpg")
    elif message.text == "Пришли анимацию(Видео)":
        bot.send_video(message.from_user.id, "Вот это поворот!.mp4")
    elif message.text == "Пришли документ":
        bot.send_document(message.from_user.id, "27-A_demo.txt")
        bot.send_message(message.from_user.id, "Вот тебе 27-ое задание егэ")
    elif message.text == "Пришли стикер":
        bot.send_message(message.from_user.id, "Не, бро, лажа, не сделано еще")
        bot.send_sticker(message.from_user.id, "CAACAgIAAxkBAAJfil-7g5saK6caYV8CsqELuWLynDH2AALiBgACOtEHAAFgVDNflxcX6h4E")
