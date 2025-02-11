import telebot
from Pie import gen_pass
import random
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я AWAXXX(version0). Напиши что-нибудь!")

@bot.message_handler(commands=['emoji'])
def gen_emodji(message):
    emodji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    bot.reply_to(message, random.choice(emodji))

@bot.message_handler(commands=['Flip'])
def flip_coin(message):
    flip = random.randint(0, 2)
    if flip == 0:
        bot.reply_to(message, "ОРЕЛ")
    else:
        bot.reply_to(message, "РЕШКА")

@bot.message_handler(commands=['Привет'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['Пока'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['Password',"Pass"])
def send_pass(message):
    bot.send_message(message.chat.id, gen_pass(10))

# Обработчик команды '/heh'
@bot.message_handler(commands=['heh', "NYHEHE"])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh)
    
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)
print("bot_started")
bot.polling()

