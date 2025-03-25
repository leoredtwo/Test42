import telebot
from Pie import gen_pass
import random
import os
import requests
print(os.listdir('images'))
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я AWAXXX(version(-4)). Напиши что-нибудь!")

@bot.message_handler(commands=['revers'])
def revers_welcome(message):
    revers_moment = message.text.split()[1]
    well = ""
    for i in range(len(revers_moment)-1,-1,-1):
        well += revers_moment[i]
    bot.reply_to(message, well)

def get_duck_image_url():    
        url = 'https://random-d.uk/api/random'
        res = requests.get(url)
        data = res.json()
        return data['url']
random.betavariate
def get_cat_image_url():    
        url = 'https://api.thecatapi.com/v1/images/search'
        res = requests.get(url)
        data = res.json()
        return data[0]['url']
random.betavariate
    
    
@bot.message_handler(commands=['duck'])
def duck(message):
    '''По команде duck вызывает функцию get_duck_image_url и отправляет URL изображения утки'''
    image_url = get_duck_image_url()
    bot.reply_to(message, image_url)

@bot.message_handler(commands=['cat'])
def cat(message):
    image_url = get_cat_image_url()
    bot.reply_to(message, image_url)


@bot.message_handler(commands=['mem'])
def send_mem(message):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:  
        bot.send_photo(message.chat.id, f)       
@bot.message_handler(commands=['Проблема экологии',"Eco","Еко"])
def send_help(message):
    bot.reply_to(message, "Этот раздел предназначен для функции свзяанные с экологией если вы хотите узнать что можно сделать из пластиковых бутылок пропишите комманду /Plastic_crafts; Что бы узнать факты про пластик пропишите /Plastic_facts")
@bot.message_handler(commands=['Plastic_crafts'])
def send_crafts(message):
    img_name = random.choice(os.listdir('plastic_crafts'))
    with open(f'plastic_crafts/{img_name}', 'rb') as f:  
        bot.send_photo(message.chat.id, f)       

@bot.message_handler(commands=['Plastic_facts'])
def gen_plfacts(message):
    Plfacts = ["С 1950-х годов человечество произвело более 8,3 миллиардов тонн пластика, и только 9% из этой массы отправились на переработку",
    "Ежегодно в океан попадает 12 миллионов тонн пластика", "В среднем человек съедает 5 граммов пластика каждую неделю. Столько же весит кредитная карта", 
    "В мире есть страны, где использование пластика карается законом. Самый строгий запрет действует в Кении: производство, продажа и использование пластиковых пакетов может обернуться тюремным сроком"          ]
    bot.reply_to(message, random.choice(Plfacts))


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
@bot.message_handler(commands=['Помогите',"Help","help"])
def send_help(message):
    bot.reply_to(message, "/Помогите, /Привет, /revers и слово (не спрашивайте о смыле этой функции), /emoji, /Flip, /heh, /Password, /Пока, /mem, /duck, /cat, /Eco")

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
    bot.reply_to(message, "Программа не распознает ваш запрос, пожалуйста воспользуйтесь коммандой /help для просмотра списка комманд")
print("bot_started")
bot.polling()
