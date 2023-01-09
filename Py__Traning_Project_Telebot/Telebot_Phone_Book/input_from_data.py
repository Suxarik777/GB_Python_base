from telebot import TeleBot, types
from func_for_work_bot import read_file, recording_file
from Token_id import TOKEN_ID

TOKEN = TOKEN_ID
bot = TeleBot(TOKEN)



def recording_str_keyboard(msg: types.Message):
    text = str(msg.text)
    data_list = text.split()
    array = read_file()
    array.append(data_list)
    recording_file(array)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1) # растяни по ширине экрана и добавь две кнопк
    button_menu = types.KeyboardButton('/menu')
    markup.add(button_menu)
    # mess = f'Привет, <b>{message.from_user.first_name} {message.from_user.last_name}</b>'
    # bot.send_message(message.chat.id, mess, parse_mode='html')
    text_message = f'Новый контакт\n{text}\n<b>записан</b>'
    bot.send_message(chat_id=msg.from_user.id, text=text_message, parse_mode='html', reply_markup=markup)