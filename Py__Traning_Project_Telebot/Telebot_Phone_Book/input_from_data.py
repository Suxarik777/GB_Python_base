from telebot import TeleBot, types
from func_for_work_bot import read_file, recording_file
from Token_id import TOKEN_ID

import emoji

TOKEN = TOKEN_ID
bot = TeleBot(TOKEN)



# работа с вводом данных в базу
@bot.message_handler(content_types=['text'])
def get_menu_input(msg: types.Message):
    menu_item = msg.text

    if menu_item == '1' or menu_item == emoji.emojize(':keyboard: с клавиатуры'):
        bot_mess = 'Введите данные в формате \nИмя Фамилия Телефон Комментарий'
        bot.send_message(chat_id=msg.from_user.id, text=bot_mess)
        bot.register_next_step_handler(msg, recording_str_keyboard)

    elif menu_item == '2' or menu_item == emoji.emojize(':file_folder: из файла'):
        bot_mess = 'Пришлите файл в формате .csv'
        bot.send_message(chat_id=msg.from_user.id, text=bot_mess)
        bot.register_next_step_handler(msg, recording_str_file)


@bot.message_handler(content_types=['text'])
def recording_str_keyboard(msg: types.Message):
    text = str(msg.text)
    data_list = text.split()
    array = read_file()
    array.append(data_list)
    recording_file(array)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1) # растяни по ширине экрана и добавь две кнопк
    button_menu = types.KeyboardButton(emoji.emojize(':scroll: Меню'))
    markup.add(button_menu)
    # mess = f'Привет, <b>{message.from_user.first_name} {message.from_user.last_name}</b>'
    # bot.send_message(message.chat.id, mess, parse_mode='html')
    text_message = f'Новый контакт\n{text}\n<b>записан</b>'
    bot.send_message(chat_id=msg.from_user.id, text=text_message, parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['documents'])
def recording_str_file(msg: types.Message):
    file_user = msg.document.file_name
    with open(file_user, 'wb') as file:
        file.write(bot.download_file(bot.get_file(msg.document.file_id).file_path))
    bot.send_message(chat_id=msg.from_user.id, text='Ваш файл принят')
    #сейчас приняв файл единожды, он его постоянно пытается обработать


