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
