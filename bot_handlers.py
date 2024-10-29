"""
Файл для определения обработчиков сообщений бота.
Содержит функции для обработки команд и обычных сообщений.
"""

import telebot
from utils import send_photo_with_keyboard
from keyboard import create_inline_keyboard

def setup_bot_handlers(bot):
    """
    Функция для установки всех обработчиков бота.
    """
    
    @bot.message_handler(commands=['start'])
    def start(message):
        """
        Обработчик команды /start.
        Отправляет приветственное сообщение с клавиатурой.
        """
        greeting = '''
Привет, уважаемый клиент! Я ваш помощник по базовым вопросам. Вот что я могу:

''' + '\n'.join([
            "/site - посетить наш сайт",
            "/help - получить информацию о моих возможностях",
            "/order - оформить быстрый заказ",
            "/contacts - получить контакты"
        ]) + '''
Выберите опцию из меню ниже:
'''
        
        send_photo_with_keyboard(bot, message.chat.id, greeting)

    @bot.callback_query_handler(func=lambda call: True)
    def handle_callback(call):
        """
        Обработчик callback запросов от инлайн-клавиатуры.
        """
        if call.data == "site":
            site_url = "https://smt-max.net/"
            bot.answer_callback_query(callback_query_id=call.id, text=f"Переход на сайт {site_url}")
            bot.send_message(chat_id=call.from_user.id, text=f"Вы были перенаправлены на сайт {site_url}")
        
        elif call.data == "actions":
            actions_text = "Доступные действия:\n/site - посетить наш сайт\n/help - получить информацию о моих возможностях\n/order - оформить быстрый заказ\n/contacts - получить контакты"
            bot.answer_callback_query(callback_query_id=call.id, text=actions_text)
            bot.send_message(chat_id=call.from_user.id, text=actions_text)
        
        elif call.data == "order":
            order_text = "Для оформления быстрого заказа, пожалуйста, отправьте мне список товаров."
            bot.answer_callback_query(callback_query_id=call.id, text=order_text)
            bot.send_message(chat_id=call.from_user.id, text=order_text)
        
        elif call.data == "help":
            help_text = '<u>Вот что я могу:</u>\n\n/site - посетить наш сайт\n/actions - узнать доступные действия\n/order - оформить быстрый заказ\n/contacts - получить контакты'
            bot.answer_callback_query(callback_query_id=call.id, text=help_text)
            bot.send_message(chat_id=call.from_user.id, text=help_text, parse_mode='html')
        
        elif call.data == "contacts":
            contacts_text = "Телефон: +7 (999) 123-45-67\nEmail: support@example.com"
            bot.answer_callback_query(callback_query_id=call.id, text=contacts_text)
            bot.send_message(chat_id=call.from_user.id, text=contacts_text)

    @bot.message_handler(commands=['help'])
    def help(message):
        """
        Обработчик команды /help.
        Отправляет информацию о возможностях бота в виде кнопок.
        """
        help_text = "Вот что я могу:"
        inline_keyboard = create_inline_keyboard()
        bot.send_message(chat_id=message.chat.id, text=help_text, reply_markup=inline_keyboard)

    @bot.message_handler()
    def info(message):
        """
        Обработчик обычных сообщений.
        """
        pass