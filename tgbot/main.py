from tokennn import token
import telebot
from database import Database

API_TOKEN = token

bot = telebot.TeleBot(API_TOKEN)
db = Database()


@bot.message_handler(commands=['start'])
def button_message(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = telebot.types.KeyboardButton("Категории")
    markup.add(item1)
    bot.send_message(message.chat.id, 'Доступно меню', reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Категории')
def category(message):
    categories_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    categories = get_categories()
    for i in categories.keys():
        item = telebot.types.KeyboardButton(i)
        categories_markup.add(item)

    bot.send_message(message.chat.id, 'Выберите категорию', reply_markup=categories_markup)


@bot.message_handler(func=lambda message: message.text in get_categories().keys())
def select_category(message):
    chosen_category = get_categories()[message.text]
    recipes = db.get_recipes_by_category(chosen_category)
    response = ''
    for recipe in recipes:
        response += f"{recipe['recipe_name']} - {recipe['recipe_url']}\n"
    bot.send_message(message.chat.id, response)


def get_categories():
    categories = db.get_categories()
    result = {}
    for category in categories:
        result[category['name']] = category['id']
    return result


bot.polling()
