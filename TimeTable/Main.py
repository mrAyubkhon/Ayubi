import telebot  # Импортируем библиотеку для работы с Telegram Bot API
import os  # Для работы с переменными окружения
from flask import Flask, request  # Импортируем Flask для работы с вебхуками
from telebot import types

# Создаём объект бота с использованием токена
TOKEN = os.getenv('7365761529:AAFYeDS9e4uWiTk9xBxDebdfs0XEX1BOcPg')  # Подключаем токен из переменных окружения для безопасности
bot = telebot.TeleBot(TOKEN)

# Создаем Flask-приложение
app = Flask(__name__)

# Обработчик команды '/start'
@bot.message_handler(commands=['start'])
def start(message):
    # Создаем клавиатуру
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

    # Создаем кнопки с днями недели, Gym и ссылкой
    btn1 = types.KeyboardButton('CS4-23')
    btn2 = types.KeyboardButton('CS5-23')
    btn3 = types.KeyboardButton('Monday')
    btn4 = types.KeyboardButton('Tuesday')
    btn5 = types.KeyboardButton('Wednesday')
    btn6 = types.KeyboardButton('Thursday')
    btn7 = types.KeyboardButton('Friday')
    btn8 = types.KeyboardButton('Gym')
    btn9 = types.KeyboardButton('Swimming Pool')
    btn10 = types.KeyboardButton('Ping Pong')
    btn11 = types.KeyboardButton('Time Table website')

    # Добавляем кнопки в клавиатуру
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11)

    # Отправляем сообщение с клавиатурой
    bot.send_message(
        message.chat.id,
        f'Hi, how can I help you, miss/mister {message.from_user.first_name} {message.from_user.last_name}. Choose a day of the <b>Week</b>,<b>Gym</b> or <b>Website</b>',
        parse_mode='HTML', reply_markup=markup
    )

# Остальные обработчики, как и раньше
@bot.message_handler(func=lambda message: message.text == 'CS4-23')
def cs423(message):
    photo = open('CS4-23.png', 'rb')  # Укажите путь к вашему фото
    bot.send_photo(message.chat.id, photo)
    photo.close()

@bot.message_handler(func=lambda message: message.text == 'CS5-23')
def cs523(message):
    photo = open('CS5-23.png', 'rb')  # Укажите путь к вашему фото
    bot.send_photo(message.chat.id, photo)
    photo.close()

@bot.message_handler(func=lambda message: message.text == 'Time Table website')
def site(message):
    bot.send_message(message.chat.id, "Here is the link to the schedule: https://cau.edupage.org/timetable/")

@bot.message_handler(func=lambda message: message.text == 'Monday')
def monday(message):
    bot.send_message(
        message.chat.id,
        f'9:30-10:50 <b>Algorithms</b> in <b>202 room</b>\n'
        f'11:00-12:20 <b>Physics</b> in <b>105 room</b>\n'
        f'13:30-14:50 <b>Software Engineering</b> in <b>104 room</b>',
        parse_mode='HTML'
    )

@bot.message_handler(func=lambda message: message.text == 'Tuesday')
def tuesday(message):
    bot.send_message(
        message.chat.id,
        f'9:30-10:50 <b>Software Engineering</b> in <b>202 room</b>\n'
        f'11:00-12:20 <b>Physics</b> in <b>104 room</b>\n'
        f'13:30-14:50 <b>Statistics for Data Science</b> in <b>202 room</b>',
        parse_mode='HTML'
    )

@bot.message_handler(func=lambda message: message.text == 'Wednesday')
def wednesday(message):
    bot.send_message(
        message.chat.id,
        f'9:30-10:50 <b>Algorithms</b> in <b>311 room</b>\n'
        f'11:00-12:20 <b>Software Engineering</b> in <b>102 room</b>',
        parse_mode='HTML'
    )

@bot.message_handler(func=lambda message: message.text == 'Thursday')
def thursday(message):
    bot.send_message(
        message.chat.id,
        f'9:30-10:50 <b>Statistics for Data Science</b> in <b>117 room</b>\n'
        f'11:00-12:20 <b>Algorithms</b> in <b>310 room</b>',
        parse_mode='HTML'
    )

@bot.message_handler(func=lambda message: message.text == 'Friday')
def friday(message):
    bot.send_message(
        message.chat.id,
        f'9:30-10:50 <b>Statistics for Data Science</b> in <b>304 room</b>\n'
        f'11:00-12:20 <b>Physics</b> in <b>413 room</b>',
        parse_mode='HTML'
    )

@bot.message_handler(func=lambda message: message.text == 'Gym')
def gym(message):
    bot.send_message(
        message.chat.id,
        f'<b>9:00-13:00</b>, <b>14:00-18:00</b> you can enter\n'
        f'Monday - Friday', parse_mode='HTML'
    )

@bot.message_handler(func=lambda message: message.text == 'Swimming Pool')
def swimming(message):
    bot.send_message(
        message.chat.id,
        f'<b>9:00-13:00</b>, <b>14:00-18:00</b> you can enter\n'
        f'Monday - Friday \n'
        f'<b>Warning: </b> you can enter if you men in <b>Monday ,Wednesday and Friday</b> in <b>14:00 - 18:00</b> \n'
        f'In <b>Tuesday</b> and <b>Thursday</b>  you can enter in <b>9:00 - 12:50 </b>', parse_mode='HTML'
    )

@bot.message_handler(func=lambda message: message.text == 'Ping Pong')
def ping_pong(message):
    bot.send_message(
        message.chat.id,
        f'<b>9:00-13:00</b>, <b>14:00-18:00</b> you can enter' , parse_mode='HTML'
    )

# Flask route для обработки вебхуков от Telegram
@app.route(f"/{TOKEN}", methods=['POST'])
def receive_update():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "!", 200

# Главная страница для проверки работы сервера
@app.route("/", methods=["GET"])
def index():
    return "Telegram bot is running!", 200

# Запуск приложения Flask (для локальной разработки и Vercel)
if __name__ == "__main__":
    app.run(debug=True)
