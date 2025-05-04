from flask import Flask
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Инициализация Flask приложения
app = Flask(__name__)

# Ваш токен для Telegram-бота
TOKEN = '8063634034:AAG9xaNnqyLjyLtk8QdF3521uy7TSrTm1EI'

# Функция для обработки команды start
def start(update: Update, context: CallbackContext):
    update.message.reply_text('Привет! Я бот.')

# Создание и настройка Updater
updater = Updater(TOKEN)

# Регистрируем обработчик команд
updater.dispatcher.add_handler(CommandHandler('start', start))

# Запуск бота
def start_bot():
    updater.start_polling()

# Маршрут для проверки работы сервера
@app.route('/')
def index():
    return "Сервер работает!"

# Запуск Flask сервера
if __name__ == "__main__":
    from threading import Thread
    # Запускаем бота в отдельном потоке
    bot_thread = Thread(target=start_bot)
    bot_thread.start()

    # Запуск Flask сервера
    app.run(host='0.0.0.0', port=5000)
