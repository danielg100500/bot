import telebot
from bot_logic import gen_pass
from bot_money import number

bot = telebot.TeleBot("8565732472:AAEJo8ytHivnZFkDR-Daqeqe8bbfexeaoOU")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Чтобы узнать, что я умею, напиши /info")

@bot.message_handler(commands=['info'])
def send_info(message):
    bot.reply_to(message, "/hello, /bye, /password, /1or2, /weather, /geo, /listwindows а ещё я умею повторять.")

@bot.message_handler(commands=['listwindows'])
def send_info(message):
    bot.reply_to(message, "Windows 1.0, Windows 2.0, Windows 3.0, Windows 89, Windows 93, Windows 95, Windows 98, Windows ME (or Millenium), Windows 2000, Windows XP, Windows Vista, Windows 7, Windows 8, Windows 9, Windows 10, Windows 11.")

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['weather'])
def weather(message):
    import requests
    city = 'Ростов - на Дону'
    url = f'http://wttr.in/{city}?format=3'
    response = requests.get(url)
    bot.send_message(message.chat.id, response.text)

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
