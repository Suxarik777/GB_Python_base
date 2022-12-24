from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *


app = ApplicationBuilder().token("5951876538:AAHOWY9XykXkI1TB1AUHlkdySAiZaJGcVfQ").build()
print('server start')

app.add_handler(CommandHandler("hi", hi_command)) #выхов метода, смотри наверх
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))

app.run_polling()