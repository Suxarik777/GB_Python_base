import emoji
from str_msg_bot import print_menu
from input_from_data import get_menu_input
from edit_data import before_get_menu_edit
from telebot import TeleBot, types
from Token_id import TOKEN_ID
from controller import get_menu

TOKEN = TOKEN_ID

bot = TeleBot(TOKEN)


# @bot.message_handler(commands=['start'])
# def start_program(msg: types.Message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2) # растяни по ширине экрана и добавь две кнопк
#     button_menu = types.KeyboardButton(emoji.emojize(':scroll: Меню'))
#     markup.add(button_menu)
#
#     mess = f'''Привет, <b>{msg.from_user.first_name} {msg.from_user.last_name}</b>
# Я создан студентом GeekBrains и я телефонная книжка
# ЖМИ кнопку "Меню"'''
#     bot.send_message(chat_id=msg.chat.id, text=mess, parse_mode='html', reply_markup=markup)
#
#     # bot.send_message(chat_id=msg.from_user.id, text=f'/start и /help - Начало работы с ботом, вывод списка комманд')
#     # bot.send_message(chat_id=msg.from_user.id, text=f'/menu - Начать работу с телефонным справочником')
#
#
#
# @bot.message_handler(content_types=['text'])
# def menu(msg: types.Message):
#     if msg.text == emoji.emojize(':scroll: Меню'):
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
#         button_input = types.KeyboardButton(emoji.emojize(':writing_hand: Ввести данные'))
#         button_edits = types.KeyboardButton(emoji.emojize(':backhand_index_pointing_right: Редактировать'))
#         markup.add(button_input, button_edits)
#         bot.send_message(chat_id=msg.chat.id, text=f'{print_menu}\n\nили жми кнопки', reply_markup=markup)
#         bot.register_next_step_handler(msg, get_menu)
#
# bot.polling(none_stop=True)