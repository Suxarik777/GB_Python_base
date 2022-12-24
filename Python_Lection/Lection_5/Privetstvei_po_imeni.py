from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None: #метод поздороваться
    await update.message.reply_text(f'Hello {update.effective_user.first_name}') 
                                    # отвечаем Hello и забираем его имя

app = ApplicationBuilder().token("5951876538:AAHOWY9XykXkI1TB1AUHlkdySAiZaJGcVfQ").build()
print('server start')

app.add_handler(CommandHandler("hello", hello)) #выхов метода, смотри наверх

app.run_polling()