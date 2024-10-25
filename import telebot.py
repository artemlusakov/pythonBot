import telebot
import re
import os
from time import sleep

# Инициализация бота
bot = telebot.TeleBot('7656211082:AAGoisBmYkH_VH2JE2lOFMNkgIUBpPJxWdQ')

# Функция для получения списка пользователей из файла
def get_users_from_file():
    users = []
    file_path = 'phon.txt'
    if os.path.exists(file_path):
        print(f"Файл {file_path} существует.")
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    # Убедимся, что строка содержит номер телефона в нужном формате
                    phone_match = re.match(r'^\+7\(\d{3}\)\d{3}-\d{2}-\d{2}$', line.strip())
                    if phone_match:
                        username = f"User_{phone_match.group(0)}"
                        user_id = int(re.sub(r'\D', '', phone_match.group(0)))
                        users.append((username, user_id))
                    else:
                        print(f"Некорректный формат данных в файле {file_path}: {line}")
            return users
        except Exception as e:
            print(f"Ошибка при чтении файла {file_path}: {str(e)}")
    else:
        print(f"Файл {file_path} не найден.")
        return []

# Функция для проверки статуса пользователя
def check_user_status(user_id):
    try:
        bot.get_chat(user_id)
        return True
    except telebot.apihelper.ApiException as e:
        if str(e).find("Forbidden") != -1:
            print(f"Пользователь {user_id} заблокировал бота или ограничил возможность отправки сообщений.")
            return False
        elif str(e).find("Chat not found") != -1:
            print(f"Чат с пользователем {user_id} не найден.")
            return False
        else:
            raise

# Функция для отправки сообщения пользователю
def send_message_to_user(user_id, message_text):
    if check_user_status(user_id):
        try:
            # Попробовать отправить сообщение напрямую с дополнительными параметрами
            bot.send_message(user_id, message_text, parse_mode='HTML', disable_web_page_preview=True)
            print(f"Сообщение успешно отправлено пользователю {user_id}")
            return True
        except Exception as e:
            print(f"Ошибка при отправке сообщения пользователю {user_id}: {str(e)}")
            return False
    else:
        print(f"Не удалось отправить сообщение пользователю {user_id}. Пользователь не найден или заблокировал бота.")
        return False

# Основная функция
def main():
    users = get_users_from_file()

    if not users:
        print("Пользователи не найдены в файле phon.txt")
        return

    message_text = "Привет! Это бот СМТ."
    
    sent_count = 0
    failed_count = 0
    
    for username, user_id in users:
        success = False
        attempts = 0
        max_attempts = 3
        
        while not success and attempts < max_attempts:
            try:
                sleep(1)  # Пауза между попытками
                success = send_message_to_user(user_id, message_text)
            except Exception as e:
                print(f"Попытка {attempts+1} не удалась для пользователя {user_id}. Ошибка: {str(e)}")
                attempts += 1
        
        if success:
            sent_count += 1
        else:
            failed_count += 1
    
    print(f"Отправлено сообщений: {sent_count}")
    print(f"Неудачных попыток отправки: {failed_count}")

# Запуск основной функции
if __name__ == "__main__":
    main()