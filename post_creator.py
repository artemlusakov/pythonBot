"""
Файл для создания постов бота.
Содержит функции для обработки команды post и создания постов.
"""

import telebot
from telebot import types

title = None
text = None
image_file_id = None
link = None

def create_post(bot, message):
    global title, text, image_file_id, link
    
    # Получаем заголовок поста
    bot.send_message(message.chat.id, "Отлично! Начнем создание поста.\nВведите заголовок поста:")
    bot.register_next_step_handler(message, lambda msg: get_post_title(bot, msg))

def get_post_title(bot, message):
    global title
    title = message.text
    bot.send_message(message.chat.id, f"Отлично! Заголовок поста: {title}\n\nТеперь введите текст поста:")
    bot.register_next_step_handler(message, lambda msg: get_post_text(bot, msg))

def get_post_text(bot, message):
    global text
    text = message.text
    bot.send_message(message.chat.id, "Отлично! Теперь отправьте фотографию для поста или нажмите кнопку 'Пропустить', если не хотите использовать изображение.")
    inline_keyboard = types.InlineKeyboardMarkup()
    skip_button = types.InlineKeyboardButton(text="Пропустить", callback_data="skip_image")
    inline_keyboard.add(skip_button)
    bot.send_message(message.chat.id, "Выберите действие:", reply_markup=inline_keyboard)
    bot.register_next_step_handler(message, lambda msg: handle_photo(bot, msg))

def handle_photo(bot, message):
    global image_file_id
    image_file_id = message.photo[-1].file_id
    bot.reply_to(message, "Изображение получено. Теперь введите ссылку для кнопки перехода:")
    bot.register_next_step_handler(message, lambda msg: get_post_link(bot, msg))

def get_post_link(bot, message):
    global link
    link = message.text
    send_post(bot, title, text, image_file_id, link)

def send_post(bot, title, text, image_file_id=None, link=None):
    keyboard = types.InlineKeyboardMarkup()
    if link:
        url_button = types.InlineKeyboardButton(text="Перейти", url=link)
        keyboard.add(url_button)
    
    if image_file_id:
        bot.send_photo(chat_id=message.chat.id, photo=image_file_id, caption=title + "\n\n" + text, reply_markup=keyboard)
    else:
        bot.send_message(chat_id=message.chat.id, text=title + "\n\n" + text, reply_markup=keyboard)
    bot.send_message(chat_id=message.chat.id, text="Пост успешно отправлен!")