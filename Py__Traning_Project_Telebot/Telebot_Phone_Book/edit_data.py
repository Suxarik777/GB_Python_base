from telebot import TeleBot, types
from func_for_work_bot import read_file, recording_file, read_index_row_data, recording_index_row_data
from Token_id import TOKEN_ID


import emoji

TOKEN = TOKEN_ID
bot = TeleBot(TOKEN)


@bot.message_handler(content_types=['text'])
def before_get_menu_edit(msg: types.Message):
    if msg.text.isdigit():
        row_numb = int(msg.text)
        recording_index_row_data(row_numb) #запоминаем значение в отдельный файл

        array = read_file()

        if row_numb >= len(array):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

            #кнопка не работает функция в контролере
            button_edits_mod = types.KeyboardButton(emoji.emojize(':backhand_index_pointing_right: повторный ввод'))
            button_menu = types.KeyboardButton(emoji.emojize(':scroll: Меню'))
            markup.add(button_edits_mod, button_menu)

            bot_mess = emoji.emojize('УПС! такой записи нет')
            bot.send_message(chat_id=msg.chat.id, text=bot_mess, reply_markup=markup)

        else:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            button_del = types.KeyboardButton(emoji.emojize(':backhand_index_pointing_right: удалить'))
            button_menu = types.KeyboardButton(emoji.emojize(':scroll: Меню'))
            markup.add(button_del, button_menu)


            red_lst = ' '.join(map(str, array[row_numb]))  # парс вложенного листа в строку
            bot_mess = f'''Что вы хотите сделать с записью? :
            '↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓'
            {red_lst}
            '↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓'
            0 - удалить
            1 - редактировать'''
            answer = bot.send_message(chat_id=msg.chat.id, text=bot_mess, reply_markup=markup)
            answer = str(answer)
            bot.register_next_step_handler(answer, get_menu_edit)



@bot.message_handler(content_types=['text'])
def get_menu_edit(msg: types.Message):
    menu_item = msg.text
    # if menu_item == '0' or menu_item == emoji.emojize(':backhand_index_pointing_right: удалить'):
    array = read_file()     # забираем записную книжку
    index_row = read_index_row_data()   # забираем индекс записи

    del array[index_row]
    recording_file(array)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    button_menu = types.KeyboardButton(emoji.emojize(':scroll: Меню'))
    markup.add(button_menu)

    bot_mess = 'ЗАПИСЬ УДАЛЕНА!'
    bot.send_message(chat_id=msg.chat.id, text=bot_mess, reply_markup=markup)



