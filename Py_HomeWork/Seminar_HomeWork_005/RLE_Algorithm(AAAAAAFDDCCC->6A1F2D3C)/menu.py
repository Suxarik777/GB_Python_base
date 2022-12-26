

def menu_user():
    print('''Меню RLE алгоритма:
    ======
    aaaasssffffff -> 4a3s6f -> aaaasssffffff
    ======
    Что вы хотите?
        1 - закодировать строку: aaaasssffffff -> 4a3s6f
        2 - декодировать строку: 4a3s6f -> aaaasssffffff
    ''')

    user_select = input('Выберите пункт меню: ')

    if user_select == '1':
        return 'coding'
    elif user_select == '2':
        return 'decoding'
    else:
        print('Ты ввел что-то не то! Попробуй ещё раз!')
        return menu_user()

