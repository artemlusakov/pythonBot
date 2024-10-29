"""
Основной файл для запуска Telegram бота.
Содержит создание экземпляра бота и запуск пуллинга.
"""

import telebot
from bot_handlers import setup_bot_handlers

TOKEN = '7656211082:AAGoisBmYkH_VH2JE2lOFMNkgIUBpPJxWdQ'
bot = telebot.TeleBot(TOKEN)

# Устанавливаем обработчики бота
setup_bot_handlers(bot)

def main():
    """
    Основная функция для запуска бота.
    Запускает бесконечную пуллинг-подсветку бота.
    """
    bot.polling(non_stop=True)

if __name__ == '__main__':
    main()