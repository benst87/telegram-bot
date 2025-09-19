import telebot

TOKEN = 'my token'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def greet(message):
    bot.reply_to(message , 'hi my name is beni')

bot.polling()