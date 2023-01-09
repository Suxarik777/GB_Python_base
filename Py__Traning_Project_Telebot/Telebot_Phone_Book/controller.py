import csv
from outputs import print_menu, menu_search, show_all, show_by_index, show_by_filter, read_file
from edits import edit
from inputs import input_menu_item, input_row, input_index, input_string
from exports import export_file, export_csv, export_xml, export_html
from telebot import TeleBot, types
from Token_id import TOKEN_ID

TOKEN = TOKEN_ID

bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_program(msg: types.Message):
    # markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2) # растяни по ширине экрана и добавь две кнопк
    # button_menu = types.KeyboardButton('Меню')
    # markup.add(button_menu)
    # mess = f'Привет, <b>{message.from_user.first_name} {message.from_user.last_name}</b>'
    # bot.send_message(message.chat.id, mess, parse_mode='html')

    bot.send_message(chat_id=msg.from_user.id, text=f'/start и /help - Начало работы с ботом, вывод списка комманд')
    bot.send_message(chat_id=msg.from_user.id, text=f'/menu - Начать работу с телефонным справочником')



@bot.message_handler(commands=['menu'])
def menu(msg: types.Message):
    bot.send_message(chat_id=msg.chat.id, text=f'{print_menu}')
    bot.register_next_step_handler(msg, get_user_menu)



def get_user_menu(msg: types.Message):
    # bot.send_message(chat_id=msg.chat.id, text=f'Я нахожусь в get_user, ваш выбор{msg.text}')
    # menu_item = input_menu_item()
    menu_item = msg.text # получаем то что ввел пользователь
    if menu_item == '1':
        bot.send_message(chat_id=msg.from_user.id, text=f'1 - ввод с клавиатуры \n2 - ввод из файла')
        bot.register_next_step_handler(msg, input_row)

def input_row(msg: types.Message):
    menu_item = msg.text
    if menu_item == '1':
        bot.send_message(chat_id=msg.from_user.id, text=f'Введите данные в формате \n"Имя;Фамилия;Телефон;Комментарий"')
        bot.register_next_step_handler(msg, recording_str_keyboard)


def recording_str_keyboard(msg: types.Message):
    text = str(msg.text)
    print('записываем текст ' + text)
    data_list = text.split()
    print(data_list)
    # array = read_file()
    # print('смотрим массив ' + array)
    # array.append(text_list)
    # print('итоговый массив' + array)


        # input_row(array)
    #     elif menu_item == 2:
    #         ch_index = input_index(array)
    #         array = edit(ch_index, array)
    # elif menu_item == 3:
#         export_item = export_file()
#         if export_item == 1:
#             export_csv(array)
#         if export_item == 2:
#             export_xml(array)
#         if export_item == 3:
#             export_html(array)
#     elif menu_item == 4:
#         menu_search()
#         search_item = input_menu_item()
#         if search_item == 1:
#             show_all(array)
#         elif search_item == 2:
#             show_item = input_menu_item()
#             show_by_index(array, show_item)
#         elif search_item == 3:
#             search_item = input_string()
#             show_by_filter(array, search_item)
# with open(f'inputs.csv', 'w', encoding='utf-8') as file:
#     for text in array:
#         res_text = ";".join(text)
#         file.writelines(f'{res_text}; \n')
# print(f"Экспорт файла input.csv завершен.")
#
bot.polling(none_stop=True)