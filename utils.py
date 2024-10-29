"""
Файл с вспомогательными функциями для бота.
Содержит функцию для отправки фото с клавиатурой.
"""

import webbrowser
from keyboard import create_inline_keyboard

def send_photo_with_keyboard(bot, chat_id, caption):
    """
    Отправляет фото с инлайн-клавиатурой в чат.
    
    Аргументы:
    bot - экземпляр бота
    chat_id - ID чата
    caption - подпись к фотографии
    
    Использует функцию create_inline_keyboard() из keyboard.py
    """
    photo_url = 'https://smt-max.net/wp-content/uploads/2024/05/Frame-215.jpg'
    inline_keyboard = create_inline_keyboard()
    bot.send_photo(chat_id, photo=photo_url, caption=caption, reply_markup=inline_keyboard)