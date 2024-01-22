import telebot
import info
import json
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

number_quest = 1
API_TOKEN = '6540054720:AAEie0nYSXq442bG8df_a1N4If4Xh72YxMQ'
bot = telebot.TeleBot(API_TOKEN)
res = {"Анатолий Сергиевский": 0, "Товарищ Молоков": 0, "Фредди Трампер": 0, "Флоренс Васси": 0, "Арбитр": 0}


@bot.message_handler(commands=['start'])
def start(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("/help"))
    markup.add(KeyboardButton("/go"))
    bot.send_message(message.chat.id, info.start_text, reply_markup=markup)


@bot.message_handler(commands=['help'])
def help(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("/start")
    keyboard.add("/help")
    keyboard.add("/go")
    keyboard.add("/restart")
    bot.send_message(message.chat.id, info.help_text, reply_markup=keyboard)


@bot.message_handler(commands=['go'])
def go(message):
    global number_quest
    user_id = message.from_user.id
    if number_quest in info.all_questions:
        question_text = info.all_questions[number_quest]["question"]
        options = info.all_questions[number_quest]["answers"].keys()

        keyboard = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        for option in options:
            keyboard.add(telebot.types.KeyboardButton(option))
        bot.send_message(message.chat.id, question_text, reply_markup=keyboard)
        save_progress(user_id, number_quest)
        bot.register_next_step_handler(message, count_res)
    else:

        view_res(message)


@bot.message_handler(commands=['restart'])
def restart(message):
    global number_quest
    number_quest = 1
    go(message)


def count_res(message):
    global number_quest
    global res
    if number_quest == 1:
        if message.text == "Да":
            res["Анатолий Сергиевский"] += 5
            res["Товарищ Молоков"] += 5
        if message.text == "Нет":
            res["Флоренс Васси"] += 3
        if message.text == "Смотря, какая цель, и какие средства":
            res["Арбитр"] += 4
    elif number_quest == 2:
        if message.text == "Исполнение моих целей":
            res["Анатолий Сергиевский"] += 5
            res["Товарищ Молоков"] += 3
            res["Фредди Трампер"] += 3
            res["Флоренс Васси"] += 1
            res["Арбитр"] += 1
        if message.text == "Только я сам(-а)":
            res["Анатолий Сергиевский"] += 2
            res["Товарищ Молоков"] += 1
            res["Фредди Трампер"] += 2
            res["Флоренс Васси"] += 5
            res["Арбитр"] += 1
        if message.text == "Когда все играют по правилам":
            res["Анатолий Сергиевский"] += 1
            res["Фредди Трампер"] += 1
            res["Флоренс Васси"] += 2
            res["Арбитр"] += 4
        if message.text == "Тепло и забота":
            res["Анатолий Сергиевский"] += 1
            res["Фредди Трампер"] += 5
            res["Флоренс Васси"] += 2
            res["Арбитр"] += 2
    elif number_quest == 3:
        if message.text == "Это окружающим нелегко со мной":
            res["Товарищ Молоков"] += 3
            res["Фредди Трампер"] += 5
        if message.text == "Да, вполне":
            res["Анатолий Сергиевский"] += 1
            res["Товарищ Молоков"] += 3
            res["Флоренс Васси"] += 4
            res["Арбитр"] += 5
        if message.text == "Достаточно сложно":
            res["Анатолий Сергиевский"] += 4
            res["Фредди Трампер"] += 3
    elif number_quest == 4:
        if message.text == "К сожалению, да":
            res["Флоренс Васси"] += 4
        if message.text == "Нет":
            res["Анатолий Сергиевский"] += 5
            res["Товарищ Молоков"] += 3
        if message.text == "Зависит от человека":
            res["Арбитр"] += 4
        if message.text == "Нет, но хочу":
            res["Фредди Трампер"] += 4
    number_quest += 1
    go(message)


def save_progress(user_id, number_quest):
    cur_progress = {str(user_id): number_quest}
    try:
        with open('progress.json', 'r') as file:
            progress = json.load(file)
        progress[str(user_id)] = number_quest
        with open('progress.json', 'w') as file:
            json.dump(progress, file)
    except:
        with open('progress.json', 'w') as file:
            json.dump(cur_progress, file)


def load_progress(user_id):
    global number_quest
    try:
        with open('progress.json', 'r') as file:
            number_quest = json.load(file)
            return number_quest.get(str(user_id))
    except FileNotFoundError:
        return None


def view_res(message):
    itog = max(res, key=res.get)
    if itog == "Фредди Трампер":
        with open("фредди.jpg", "rb") as f:
            keyboard = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
            keyboard.add("/restart")
            bot.send_photo(message.chat.id, f, info.freddie, reply_markup=keyboard)
    elif itog == "Анатолий Сергиевский":
        with open("толя.jpg", "rb") as f:
            keyboard = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
            keyboard.add("/restart")
            bot.send_photo(message.chat.id, f, info.tolya, reply_markup=keyboard)
    elif itog == "Товарищ Молоков":
        with open("молоков.jpg", "rb") as f:
            keyboard = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
            keyboard.add("/restart")
            bot.send_photo(message.chat.id, f, info.molokov, reply_markup=keyboard)
    elif itog == "Флоренс Васси":
        with open("флоренс.jpg", "rb") as f:
            keyboard = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
            keyboard.add("/restart")
            bot.send_photo(message.chat.id, f, info.florence, reply_markup=keyboard)
    elif itog == "Арбитр":
        with open("арбитр.jpg", "rb") as f:
            keyboard = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
            keyboard.add("/restart")
            bot.send_photo(message.chat.id, f, info.arbitr, reply_markup=keyboard)


bot.polling()
