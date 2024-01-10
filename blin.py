import telebot
import random
import info

# Создаём бота
API_TOKEN = '6540054720:AAEie0nYSXq442bG8df_a1N4If4Xh72YxMQ'
bot = telebot.TeleBot(API_TOKEN)

# Изначально пользователей нет, пустой словарь
user_data = {}

# Начало работы, спрашиваем возраст
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я умею рекомендовать игры.")
    bot.send_message(message.chat.id, "Пожалуйста, скажи, сколько тебе лет?")

# Если возраст уже указан, рекомендуем игру
@bot.message_handler(commands=['game'])
def game(message):
    # Получаем `user_id` пользователя
    user_id = message.from_user.id

    # Проверяем, что user_id пользователя есть в словаре
    # Если нет -- просим прислать свой возраст
    if user_id not in user_data:
        bot.send_message(message.chat.id, "Пожалуйста, пришли сначала свой возраст.")
    elif user_data[user_id]["age"] < 13:
        bot.send_message(message.chat.id, random.choice(info.younger_than_13))
    elif 13 <= user_data[user_id]["age"] < 18:
        bot.send_message(message.chat.id, random.choice(info.younger_than_18))
    else:
        bot.send_message(message.chat.id, random.choice(info.older_than_18))

@bot.message_handler(commands=['hello'])
def hello(message):
    username = message.from_user.first_name
    bot.send_message(message.chat.id, text=f"Привет, {username}!")
# Запоминаем присланный возраст
@bot.message_handler()
def save_age(message):
    # Проверяем, что возраст - число
    if not message.text.isdigit():
        bot.send_message(message.chat.id, "Пожалуйста, пришли свой возраст цифрами.")
    else:
        user_id = message.from_user.id
        # Запоминаем присланный возраст в локальную переменную `age`
        age = int(message.text)
        # Сохраняем возраст пользователя в словарь по `user_id`
        user_data[user_id] = {}
        user_data[user_id]['age'] = age
        # Сохраняем имя пользователя в словарь по `user_id`
        user_data[user_id]['name'] = message.from_user.first_name

        bot.send_message(message.chat.id, "Отлично, я запомнил! Теперь можешь использовать команду /game")

# Запускаем бота
bot.polling()
