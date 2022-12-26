from imports import view_playing_area


def user_input_position(who_gamer, user_name_1, user_name_2, max_pos=9):
    view_playing_area('enumerate_playing_area')
    user_name = str()
    if who_gamer == 'user_1':
        user_name == user_name_1
    elif who_gamer == 'user_2':
        user_name == user_name_2

    user_input = int(input(f'{user_name} введите позицию на доске: '))
    if 1 <= user_input <= max_pos:
        return user_input
    else:
        print('УПС! Что-то пошло не так!')
        return user_input_position(who_gamer, user_name_1, user_name_2, max_pos)


def index_pos_line(pos):
    if pos in {1, 2, 3}:
        return 0
    elif pos in {4, 5, 6}:
        return 2
    elif pos in {7, 8, 9}:
        return 4


def index_pos_row(pos):
    if pos in {1, 4, 7}:
        return 0
    elif pos in {2, 5, 8}:
        return 2
    elif pos in {3, 6, 9}:
        return 4


def user_name_1():
    name = input('Твой ник игрок №1?: ')
    print('Отлично ты играешь за крестики: + ')
    return name


def user_name_2():
    name = input('Твой ник игрок №2?: ')
    print('Ну а тебе достаются нолики: 0 ')
    return name


def user_symbol(who_gamer):
    if who_gamer == 'user_1':
        return '+'
    elif who_gamer == 'user_2':
        return '0'
