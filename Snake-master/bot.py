import telebot
from telebot import types
import database

bot = telebot.TeleBot("6238291301:AAEtIt8gs2cFHrKELu9D7AF7LfNqP9yAU30")

@bot.message_handler(commands=['start'])

def start_message(message):
    bot.send_message(message.chat.id, "Hello, for command list type /command")

@bot.message_handler(commands=['command'])

def help_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Player table")
    btn2 = types.KeyboardButton("Github")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, "Choose command", reply_markup=markup)

@bot.message_handler()

def stats_message(message):
    if message.text == "Player table":
        data = database.show_table()
        for i in range(len(data)):
            bot.send_message(message.chat.id, f"{i + 1}) {data[i][0]}: {data[i][2]}")
    elif message.text == "Github":
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Github link", url='https://github.com')
        markup.add(button1)
        bot.send_message(message.chat.id, "Click to the link", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, message.text)


bot.polling()