from telebot import TeleBot, types


print_menu = 'Введите номер команды:\n1: Ввод\n2: Редактирование\n3: Экспорт\n4: Вывод\n7: Выйти'


def hi_bot(msg: types.Message):
    hi_am_bot = f'''Привет, <b>{msg.from_user.first_name} {msg.from_user.last_name}</b>

Я создан студентом GeekBrains и я телефонная книжка

ЖМИ кнопку "Меню"'''