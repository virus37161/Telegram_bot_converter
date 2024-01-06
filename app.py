import telebot
from config import keys, TOKEN
from utils import Exceptionn, Converter

bot = telebot.TeleBot(TOKEN)




@bot.message_handler(commands=['values'])
def values(message):
    text = "Доступные валюты:"
    for i in keys.keys():
        text = '\n'.join((text, i, ))
    bot.reply_to(message, text)

@bot.message_handler(commands=['start', 'help'])
def starter(message):
    bot.reply_to(message, "Чтобы узнать стоимость валюты напишите боту на русском языке <имя валюты, \
цену которой он хочет узнать> <имя валюты, в которой надо узнать цену первой валюты> <количество первой валюты>\nУвидеть список доступных валют:/values")

@bot.message_handler(content_types=['text'])
def convert (message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise Exceptionn("Неверное количество параметров")

        quote, base, amount = values
        text = Converter.convert(quote, base, amount)
    except Exceptionn as e:
        bot.reply_to(message, f"Ошибка:\n{e}")
    except Exception as e:
        bot.reply_to(message,f"Ошибка:\n{e}")
    else:
        bot.send_message(message.chat.id, f"Cтоимость {amount} {keys.get(quote)} cоставляет - {round(float(text) * float(amount), 2)} {keys.get(base)}")

bot.polling()


