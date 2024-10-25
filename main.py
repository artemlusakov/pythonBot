import telebot
import webbrowser

bot=telebot.TeleBot('7656211082:AAGoisBmYkH_VH2JE2lOFMNkgIUBpPJxWdQ')
@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open("https://smt-max.net/")

# функция для вывода текста при вводе команды /start
@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'Привет! {message.from_user.first_name}')

# функция для вывода текста при вводе команды /help
@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id,'<u>Вот что я могу</u> /site посетить сайт ', parse_mode='html')


# Смотри и запомни такие условия лучше всего пихать в конц а именно @bot.message_handler() т.к мы должны обрабатывать текст юзера а не команды
@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет! {message.from_user.first_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID {message.from_user.id}')

bot.polling(non_stop=True)