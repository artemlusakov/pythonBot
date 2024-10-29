# Импортируем необходимые модули и типы данных
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import webbrowser

# Создаем экземпляр бота с токеном
bot = telebot.TeleBot('7656211082:AAGoisBmYkH_VH2JE2lOFMNkgIUBpPJxWdQ')

# Функция для создания инлайн-клавиатуры
def create_inline_keyboard():
    # Создаем объект InlineKeyboardMarkup
    inline_keyboard = InlineKeyboardMarkup()
    # Устанавливаем ширину каждой строки клавиатуры
    inline_keyboard.row_width = 2
    
    # Добавляем кнопки в одну строку
    inline_keyboard.add(
        InlineKeyboardButton(text="Наш сайт", callback_data="site"),
        InlineKeyboardButton(text="Наши акции", callback_data="actions")
    )
    inline_keyboard.add(
        InlineKeyboardButton(text="Оформить быстрый заказ", callback_data="order"),
        InlineKeyboardButton(text="Помощь", callback_data="help")
    )
    inline_keyboard.add(
        InlineKeyboardButton(text="Контакты", callback_data="contacts")
    )
    
    return inline_keyboard

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    # Создаем приветственное сообщение
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
    
    # Создаем инлайн-клавиатуру
    inline_keyboard = create_inline_keyboard()
    
    # Отправляем фото с клавиатурой
    bot.send_photo(message.chat.id, photo='https://smt-max.net/wp-content/uploads/2024/05/Frame-215.jpg', caption=greeting, reply_markup=inline_keyboard)

# Обработчик callback запросов
@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    # Определяем действие для каждого типа кнопки
    if call.data == "site":
        site_url = "https://smt-max.net/"
        # Отвечаем на callback запрос
        bot.answer_callback_query(callback_query_id=call.id, text=f"Переход на сайт {site_url}")
        
        try:
            # Пытаемся открыть сайт в браузере
            webbrowser.open(site_url)
            # Отправляем сообщение пользователю
            bot.send_message(chat_id=call.from_user.id, text=f"Вы были перенаправлены на сайт {site_url}")
        except Exception as e:
            # Если возникла ошибка при открытии сайта
            bot.send_message(chat_id=call.from_user.id, text=f"Произошла ошибка при открытии сайта: {str(e)}")
    
    elif call.data == "actions":
        actions_text = "Доступные действия:\n/site - посетить наш сайт\n/help - получить информацию о моих возможностях"
        # Отвечаем на callback запрос
        bot.answer_callback_query(callback_query_id=call.id, text=actions_text)
        # Отправляем сообщение пользователю
        bot.send_message(chat_id=call.from_user.id, text=actions_text)
    
    elif call.data == "order":
        order_text = "Для оформления быстрого заказа, пожалуйста, отправьте мне список товаров."
        # Отвечаем на callback запрос
        bot.answer_callback_query(callback_query_id=call.id, text=order_text)
        # Отправляем сообщение пользователю
        bot.send_message(chat_id=call.from_user.id, text=order_text)
    
    elif call.data == "help":
        help_text = '<u>Вот что я могу:</u>\n\n/site - посетить наш сайт\n/actions - узнать доступные действия\n/order - оформить быстрый заказ\n/contacts - получить контакты'
        # Отвечаем на callback запрос
        bot.answer_callback_query(callback_query_id=call.id, text=help_text)
        # Отправляем сообщение пользователю
        bot.send_message(chat_id=call.from_user.id, text=help_text, parse_mode='html')
    
    elif call.data == "contacts":
        contacts_text = "Телефон: +7 (999) 123-45-67\nEmail: support@example.com"
        # Отвечаем на callback запрос
        bot.answer_callback_query(callback_query_id=call.id, text=contacts_text)
        # Отправляем сообщение пользователю
        bot.send_message(chat_id=call.from_user.id, text=contacts_text)

# Обработчик команды /help
@bot.message_handler(commands=['help'])
def help(message):
    # Создаем текст помощи
    help_text = '<u>Вот что я могу:</u>\n\n/site - посетить наш сайт\n/actions - узнать доступные действия\n/order - оформить быстрый заказ\n/contacts - получить контакты'
    # Отправляем сообщение с HTML-форматированием
    bot.send_message(message.chat.id, help_text, parse_mode='html')

# Обработчик всех остальных сообщений
@bot.message_handler()
def info(message):
    # Проверяем, является ли сообщение приветом
    if message.text.lower() == 'привет':
        # Отправляем приветственное сообщение
        bot.reply_to(message, f'Привет! {message.from_user.first_name}')
    # Проверяем, является ли сообщение запросом ID
    elif message.text.lower() == 'id':
        # Отправляем ID пользователя
        bot.reply_to(message, f'ID {message.from_user.id}')
    # Проверяем, начинается ли сообщение с '/site'
    elif message.text.lower().startswith('/site'):
        # Отправляем информацию о сайте
        site_url = 'https://smt-max.net/'
        bot.send_message(message.chat.id, f'Вы можете посетить наш сайт по следующему адресу:\n{site_url}', parse_mode='Markdown')
    # Проверяем, начинается ли сообщение с '/help'
    elif message.text.lower().startswith('/help'):
        # Отправляем текст помощи
        help_text = '<u>Вот что я могу:</u>\n\n/site - посетить наш сайт\n/actions - узнать доступные действия\n/order - оформить быстрый заказ\n/contacts - получить контакты'
        bot.send_message(message.chat.id, help_text, parse_mode='html')

# Запускаем бесконечную пуллинг-подсветку бота
bot.polling(non_stop=True)