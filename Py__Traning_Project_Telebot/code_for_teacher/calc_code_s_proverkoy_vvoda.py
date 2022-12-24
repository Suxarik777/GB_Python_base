# https://pastebin.com/Z4HJ7hz8

# python -m pip install pytelegrambotapi

from telebot import TeleBot, types
import os
 
TOKEN = ''
 
bot = TeleBot(TOKEN)
 
 
# Функция для сохранения документа, отправленного боту
@bot.message_handler(content_types=['document'])
def answer(msg: types.Message):
    filename = msg.document.file_name
    with open(filename, 'wb') as file:
        file.write(bot.download_file(bot.get_file(msg.document.file_id).file_path))
    bot.send_message(chat_id=msg.from_user.id, text='Вывожу логыыыы')
 
    # Можете раскомментировать, если потребуется затем удалять файл после обработки,
    # чтобы не тратить память.
    # Не забудьте импортировать os
    # os.remove(filename) - удаление принятого файла
 
 
dct = {} # создаём словарик в котором будем по id пользователя хранить введёные им значение ещё и в lst
@bot.message_handler(commands=['start', 'help'])
def answer(msg: types.Message):
    dct[msg.from_user.id] = [] # и при старте по его айди словарика кладём пустой список
    bot.send_message(chat_id=msg.from_user.id, text=f'Здравствуйте. Введите число')
 
 
@bot.message_handler(commands=['log'])
def answer(msg: types.Message):
    bot.send_message(chat_id=msg.from_user.id, text='Вывожу лог')
 
 
@bot.message_handler()
def answer(msg: types.Message):
    id_ = msg.from_user.id # этой переменной просто кладём его id в сокращённую переменную
    text = msg.text # тоже самое, переменная для красоты
    if len(dct[id_]) == 0: # если пользователь ничего не написал
        # if text.isdigit() # была проверка только для int чисел
        if text.count('.') <= 1 and text.replace('.', '').isdigit():
            # в тексте есть точка и при замене точки на постоту там число
            dct[id_].append(float(text)) # в словарик по id пользователя кладём в списко text пользователя
            bot.send_message(chat_id=msg.from_user.id, text=f'Введите второе число')
        else:
            bot.send_message(chat_id=msg.from_user.id, text=f'Ошибка. Введите число')
    elif len(dct[id_]) == 1: # или там один список уже есть
        if text.count('.') <= 1 and text.replace('.', '').isdigit():
            bot.send_message(chat_id=msg.from_user.id, text=f'Результат: {float(text) + dct[id_][0]}')
            dct[id_].clear()
        else:
            bot.send_message(chat_id=msg.from_user.id, text=f'Ошибка. Введите число')
 
 
bot.polling()