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

# telegram chatbot with dialogflow and pytelegramapi

import os  # os

import google.cloud.dialogflow_v2 as dialogflow  # dialogflow
import telebot  # pytelegramapi

# telegram bot token
bot = telebot.TeleBot('5889249524:AAHBfPSZWsPe9vygYzl4EqMp3WuE3cYG-Jc')

# dialogflow project id
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "papazakon-plmm-d6606782053a.json"
DIALOGFLOW_PROJECT_ID = 'papazakon-plmm'
DIALOGFLOW_LANGUAGE_CODE = 'ru'
SESSION_ID = 'me'


# start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Привет, я бот. Чем могу помочь?')


# text message handler
@bot.message_handler(func=lambda message: True)
def send_text(message):
    text_to_be_analyzed = message.text
    response = detect_intent_texts(DIALOGFLOW_PROJECT_ID, SESSION_ID, text_to_be_analyzed, DIALOGFLOW_LANGUAGE_CODE)
    bot.reply_to(message, response.query_result.fulfillment_text)


# dialogflow function
def detect_intent_texts(project_id, session_id, text, language_code):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)
    text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.types.QueryInput(text=text_input)
    response = session_client.detect_intent(session=session, query_input=query_input)
    return response


# run bot
bot.polling()
