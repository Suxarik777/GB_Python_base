import csv
from outputs import menu_search, show_all, show_by_index, show_by_filter
from edits import edit
from inputs import input_menu_item, input_row, input_index, input_string
from exports import export_file, export_csv, export_xml, export_html
from func_for_work_bot import read_file, recording_file
import emoji
from str_msg_bot import print_menu
from input_from_data import recording_str_keyboard
from telebot import TeleBot, types
from Token_id import TOKEN_ID

TOKEN = TOKEN_ID

bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_program(msg: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2) # растяни по ширине экрана и добавь две кнопк
    button_menu = types.KeyboardButton(emoji.emojize(':scroll: Меню'))
    markup.add(button_menu)

    mess = f'''Привет, <b>{msg.from_user.first_name} {msg.from_user.last_name}</b>
Я создан студентом GeekBrains и я телефонная книжка
ЖМИ кнопку "Меню"'''
    bot.send_message(chat_id=msg.chat.id, text=mess, parse_mode='html', reply_markup=markup)

    # bot.send_message(chat_id=msg.from_user.id, text=f'/start и /help - Начало работы с ботом, вывод списка комманд')
    # bot.send_message(chat_id=msg.from_user.id, text=f'/menu - Начать работу с телефонным справочником')



@bot.message_handler(content_types=['text'])
def menu(msg: types.Message):
    if msg.text == emoji.emojize(':scroll: Меню'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        button_input = types.KeyboardButton(emoji.emojize(':writing_hand: Ввести данные'))
        markup.add(button_input)
        bot.send_message(chat_id=msg.chat.id, text=f'{print_menu}\n\nили жми кнопки', reply_markup=markup)
        bot.register_next_step_handler(msg, get_menu)


# работа с выбором пользователя по меню
def get_menu(msg: types.Message):
    # bot.send_message(chat_id=msg.chat.id, text=f'Я нахожусь в get_user, ваш выбор{msg.text}')
    # menu_item = input_menu_item()
    menu_item = msg.text # получаем то что ввел пользователь
    if menu_item == '1' or menu_item == emoji.emojize(':writing_hand: Ввести данные'):

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        button_input_keyboard = types.KeyboardButton(emoji.emojize(':keyboard: с клавиатуры'))
        button_input_file = types.KeyboardButton(emoji.emojize(':file_folder: из файла'))
        button_menu = types.KeyboardButton(emoji.emojize(':scroll: Меню'))
        markup.add(button_input_keyboard, button_input_file, button_menu)

        bot_mess = '1 - ввод с клавиатуры \n2 - ввод из файла\n\nили жми кнопки'
        bot.send_message(chat_id=msg.from_user.id, text=bot_mess, reply_markup=markup)
        bot.register_next_step_handler(msg, get_menu_input)


# работа с вводом данных в базу
def get_menu_input(msg: types.Message):
    menu_item = msg.text
    if menu_item == '1' or menu_item == emoji.emojize(':keyboard: с клавиатуры'):
        bot_mess = 'Введите данные в формате \nИмя Фамилия Телефон Комментарий'
        bot.send_message(chat_id=msg.from_user.id, text=bot_mess)
        bot.register_next_step_handler(msg, recording_str_keyboard)
    elif menu_item == emoji.emojize(':scroll: Меню'):
        bot.register_next_step_handler(msg, menu)


# def recording_str_keyboard(msg: types.Message):
#     text = str(msg.text)
#     data_list = text.split()
#     array = read_file()
#     array.append(data_list)
#     recording_file(array)


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