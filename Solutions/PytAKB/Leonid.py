import telebot
import random
import requests
from token import TOKEN 

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands = ["start"])
def start(message):
    bot.send_message(message.chat.id, "Привет")

@bot.message_handler(commands=["coffee"])
def coffee(message): 
    r = requests.get("https://coffee.alexflipnote.dev/random.json").json()
    img = r["file"]
    bot.send_photo(message.chat.id, img)

#@bot.message_handler(func = lambda x: "/rand" in x.text)
@bot.message_handler(commands=["rand"])
def send_random(message):
    bot.send_message(message.chat.id, f"случайное число - {random.randint(0, 100)}") 

@bot.message_handler(content_types = ["text"])
def echo(message):
    duplicated_text = message.text
    bot.send_message(message.chat.id, duplicated_text)

if __name__ == "__main__":
    bot.infinity_polling()