import os
import telebot
import requests
import random
from bot_logic import gen_pass
from bot_money import number

bot = telebot.TeleBot("8565732472:AAEJo8ytHivnZFkDR-Daqeqe8bbfexeaoOU")

print(os.listdir('images'))

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Чтобы узнать, что я умею, напиши /info")

@bot.message_handler(commands=['info'])
def send_info(message):
    bot.reply_to(message, "/hello, /bye, /password, /1or2, /weather, /geo, /listwindows, /dance, /system, /system2, /random_system, /duck, /dog, /pokemon, /fox, а ещё я умею повторять.")

@bot.message_handler(commands=['listwindows'])
def send_info(message):
    bot.reply_to(message, "Windows 1.0, Windows 2.0, Windows 3.0, Windows 89, Windows 93, Windows 95, Windows 98, Windows ME (or Millenium), Windows 2000, Windows XP, Windows Vista, Windows 7, Windows 8, Windows 9, Windows 10, Windows 11.")

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['feel'])
def send_feel(message):
    bot.reply_to(message, "Как дела?")

@bot.message_handler(commands=['dance'])
def send_dance(message):
    image_url="https://masterpiecer-images.s3.yandex.net/85be56ac526311eebffbbadf81d486ab:upscaled"
    bot.send_photo(message.chat.id, photo=image_url)

@bot.message_handler(commands=['system2'])
def send_ranimg(message):
    with open('images/system2.jpg', 'rb') as f:  
        bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=['system'])
def send_sun(message):
    bot.send_photo(message.chat.id, open("images/system.png", 'rb'))

@bot.message_handler(commands=['random_system'])
def send_sunny(message):
    photo = random.choice(['system.png','system2.jpg'])
    # file_path = 'images/' + photo
    file_path = f'images/{photo}'
    bot.send_photo(message.chat.id, open(file_path, 'rb'))

@bot.message_handler(commands=['weather'])
def weather(message):
    city = 'Ростов - на Дону'
    url = f'http://wttr.in/{city}?format=3'
    response = requests.get(url)
    bot.send_message(message.chat.id, response.text)

def get_duck_image_url():    
        url = 'https://random-d.uk/api/random'
        res = requests.get(url)
        data = res.json()
        return data['url']

@bot.message_handler(commands=['duck'])
def duck(message):
    '''По команде duck вызывает функцию get_duck_image_url и отправляет URL изображения утки'''
    image_url = get_duck_image_url()
    bot.reply_to(message, image_url)

def get_dog_image_url():    
        url = 'https://random.dog/woof.json'
        res = requests.get(url)
        data = res.json()
        return data['url']

@bot.message_handler(commands=['dog'])
def dog(message):
    '''По команде dog вызывает функцию get_dog_image_url и отправляет URL изображения собаки'''
    image_url = get_dog_image_url()
    bot.reply_to(message, image_url)

def get_pokemon_image_url():
        pokemons = ['pikachu', 'ditto', 'slowpoke']
        random_pokemon = random.choice(pokemons)
        url = f'https://pokeapi.co/api/v2/pokemon/{random_pokemon}'
        res = requests.get(url)
        data = res.json()
        return data['sprites']['front_default']

@bot.message_handler(commands=['pokemon'])
def pokemon(message):
    '''По команде pokemon вызывает функцию get_pokemon_image_url и отправляет URL изображения собаки'''
    image_url = get_pokemon_image_url()
    bot.reply_to(message, image_url)

def get_fox_image_url():    
        url = 'https://randomfox.ca/floof/'
        res = requests.get(url)
        data = res.json()
        return data['image']

@bot.message_handler(commands=['fox'])
def fox(message):
    '''По команде dog вызывает функцию get_fox_image_url и отправляет URL изображения лисы'''
    image_url = get_fox_image_url()
    bot.reply_to(message, image_url)

@bot.message_handler(commands=['geo'])
def send_geo(message):
    bot.send_location(message.chat.id, 55.7558, 37.6173)
    bot.send_message(message.chat.id, "📍 Москва, Кремль")

@bot.message_handler(commands=['password'])
def password(message):
    qqq = gen_pass(10)
    bot.reply_to(message, gen_pass(10))

@bot.message_handler(commands=['1or2'])
def money(message):
    uuu = number()
    bot.reply_to(message, number())

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()
