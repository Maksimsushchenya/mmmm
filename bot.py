import config
import telebot
from pycbrf import ExchangeRates
from datetime import date
from telebot import types

today = date.today()

rates = ExchangeRates(today)
bot = telebot.TeleBot(config.TOKEN)

menu=types.ReplyKeyboardMarkup( resize_keyboard=True)

btnUSD = types.KeyboardButton(text="us Доллар США")

menu.add(btsUSD)
@bot.message_handler(commands=["start"])
def start(message):

	@bot.message_handler(message.chat.id,"Выбери валюту:", reply_markup=menu)
	
@bot.message_handler(func = lambda message: message.text=='🇺🇸 Доллар США')
def usd(message):
	text = "1 Доллар США ="+str(rates['USD'].rate)+"руб."
	bot.send_message(message.chat.id, text)
	if __name__ == '__main__':
		bot.infinity_polling()