# accaunt My_gultcev_bot

from telebot import TeleBot, types

TOKEN = '5812598837:AAGTzxKkduU80H_7Uc2csFq7CAU3iJXBgx0'

bot = TeleBot(TOKEN)


@bot.message_handler()
def answer(msg: types.Message):    # бот ждут сообщение
 
    text = msg.text # получаем сообщение
 
    if int(text) % 2 == 0:
        bot.register_next_step_handler(msg, answer1)
    else:
        bot.register_next_step_handler(msg, answer2)
 
    bot.send_message(chat_id=msg.from_user.id, text='Вы прислали: ' + msg.text)
 
 
def answer1(msg):
    bot.send_message(chat_id=msg.from_user.id, text='Вы ввели чётное число')
 
 
def answer2(msg):
    bot.send_message(chat_id=msg.from_user.id, text='Вы ввели нечётное число')
 

bot.polling()