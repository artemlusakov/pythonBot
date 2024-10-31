import sqlite3
import telebot

bot = telebot.TeleBot('7656211082:AAGoisBmYkH_VH2JE2lOFMNkgIUBpPJxWdQ')

@bot.message_handler(commands=['start'])
def start(message):
    conn =sqlite3.connect('Bd.sql')
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF ')