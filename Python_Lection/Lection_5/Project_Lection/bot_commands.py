from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
from spy_log import log

async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE): #метод поздороваться
    log(update, context) # вызываем функцию из блока с функцией spy_log
    await update.message.reply_text(f'Hi!!! {update.effective_user.first_name}') 
                                    # отвечаем Hello и забираем его имя

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context) 
    await update.message.reply_text(f'/hi\n/time\n/help\n/sum')

async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context) 
    await update.message.reply_text(f'{datetime.datetime.now().time()}') 

async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context) 
    msg = update.message.text # берем сообщение пользователя и кладем в отдельную переменную
    print(msg)
    items = msg.split() # кладём полученной сообщение в список сплитим через пробел
            #/sum 5555 2342342 (мы получаем три порции элементов в списке)
    x = int(items[1]) # разбираем элементы
    y = int(items[2])
    result = x + y
    await update.message.reply_text(f'{x} + {y} = {result}') 