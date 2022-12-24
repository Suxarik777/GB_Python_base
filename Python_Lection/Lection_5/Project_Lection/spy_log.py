from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os





async def log(update: Update, context: ContextTypes.DEFAULT_TYPE): 
    os.chdir(os.path.dirname(file)) # вспоминаем позволяет оставить файл в этом корне
    file = open('db.csv', 'a') # создаём файл и дозаписываем "a"
    file.write(f'{update.effective_user.first_name}, {update.effective_user.id}, {update.message.text}\n')# вписываем строку
                    # вспоминаем что это команда текущего Usera
    file.close()