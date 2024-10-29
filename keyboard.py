"""
Файл для создания инлайн-клавиатуры.
Содержит функцию для генерации клавиатуры с кнопками.
"""

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def create_inline_keyboard():
    """
    Создает инлайн-клавиатуру с двумя столбцами и тремя строками кнопок.
    
    Возвращает объект InlineKeyboardMarkup.
    """
    inline_keyboard = InlineKeyboardMarkup(row_width=2)
    
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