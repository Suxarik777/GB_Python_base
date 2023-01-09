from telebot import TeleBot, types

TOKEN = "5887466076:AAH1nPfW6HgRUAXXg0Hraf2l3395ZrLFy_A"

bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def answer(msg: types.Message):
    lst = ['+', '-']
    bot.send_message(chat_id=msg.from_user.id, text=f'Введите арифметическую операцию \n{" ".join(lst)}')


bot.polling()