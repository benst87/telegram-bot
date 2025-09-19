import telebot

TOKEN = '8483511071:AAEm8d1iVC7I0FbEWmRM1oyb3_sgibFIDIU'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def greet(message):
    bot.reply_to(message , 'hi my name is beni')

bot.polling()