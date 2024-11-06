"""
Файл для определения обработчиков сообщений бота.
Содержит функции для обработки команд и обычных сообщений.
"""

from utils import send_photo_with_keyboard
from keyboard import create_inline_keyboard
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

def setup_bot_handlers(bot):
    """
    Функция для установки всех обработчиков бота.
    """

    @bot.message_handler(commands=['start'])
    def start(message):
        greeting = '''
Привет, уважаемый клиент! Я ваш помощник по базовым вопросам. Вот что я могу:
Выберите опцию из меню ниже:
'''
        send_photo_with_keyboard(bot, message.chat.id, greeting)

    @bot.callback_query_handler(func=lambda call: True)
    def handle_callback(call):
        """
        Обработчик callback запросов от инлайн-клавиатуры.
        """
        if call.data == "help":
            help_text = "Вот что я могу:"
            inline_keyboard = create_inline_keyboard()
            bot.answer_callback_query(callback_query_id=call.id, text="Показано справка.")
            bot.send_message(chat_id=call.from_user.id, text=help_text, reply_markup=inline_keyboard)
        
        elif call.data == "actions":
            actions_text = "Доступные действия:\n/site - посетить наш сайт\n/help - получить информацию о моих возможностях\n/order - оформить быстрый заказ\n/contacts - получить контакты"
            # bot.answer_callback_query(callback_query_id=call.id, text=actions_text)
            bot.send_message(chat_id=call.from_user.id, text=actions_text)
        
        elif call.data == "order":
            # Создаем кнопку для перехода на другой бот
            switch_to_bot_button = InlineKeyboardButton(text="Перейти к поддержке", url=f"https://t.me/{'SmtMaxAssistantbot'}")
            markup = InlineKeyboardMarkup().add(switch_to_bot_button)

            order_text = "Обращение с поддержкой происходит с помощью второго бота компании для вашей безопасности в случае повторноно вопроса воспользуйтесь меню или напишите /start"
            bot.send_message(chat_id=call.from_user.id, text=order_text, reply_markup=markup)
            
        
        elif call.data == "contacts":
            contacts_text = "Телефон: +7 (999) 123-45-67\nEmail: support@example.com"
            # bot.answer_callback_query(callback_query_id=call.id, text=contacts_text)
            bot.send_message(chat_id=call.from_user.id, text=contacts_text)
        
        elif call.data == "site":
            site_button = InlineKeyboardButton(text="Перейти на сайт", url="https://smt-max.net/")
            markup = InlineKeyboardMarkup().add(site_button)
            bot.send_message(chat_id=call.from_user.id, text="Нажмите на кнопку для перехода на сайт", reply_markup=markup)


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
