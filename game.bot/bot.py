from secrets import choice
import telebot
from telebot import types
from config import TOKEN
from main import varianat_game, sticker


APP_URL = f'https://siliconvalleybot.herokuapp.com/'
server = (__name__)
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    text = "Здарова, Давай сыграем 'Камень-Ножница-Бумага"
    bot.send_message(message.chat.id, text)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('👊🏻')
    item2 = types.KeyboardButton('✌🏻')
    item3 = types.KeyboardButton('✋🏻')

    markup.add(item1, item2, item3)
    text = 'Выбери действие'
    bot.send_message(message.chat.id, text, reply_markup=markup)

@server.route('/')
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=APP_URL)
    return '!', 200

if __name__ == '__main__':
    server.run(host='0.0.0.0', port=int('PORT', 5000))

@bot.message_handler(content_types=['text'])
def lol(message):
    if message.chat.type=='private':
        if message.text=='👊🏻':
            result=varianat_game(1)
            bot.send_message(message.chat.id, result[1])
            bot.send_sticker(message.chat.id, sticker(result[0]))
        elif message.text=='✌🏻':
            result=varianat_game(2)
            bot.send_message(message.chat.id, result[1])
            bot.send_sticker(message.chat.id, sticker(result[0]))
        elif message.text=='✋🏻':
            result=varianat_game(3)
            bot.send_message(message.chat.id, result[1])
            bot.send_sticker(message.chat.id, sticker(result[0]))
        else:
            bot.send_message(message.chat.id, 'не тот эмодзи')

bot.polling(non_stop=True)