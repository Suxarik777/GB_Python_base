from welcom_rules import welcom
from whose_movie import random_movie
from brains_bot import bot_login
from us_input import user_login
from winner import print_winner

CANDIES = 100


def start_system():
    count_candies = CANDIES
    welcom()
    whose_move = random_movie() # return 'user_login' && 'bot_login'

    print(f'\nНа столе {count_candies} кофеты')

    while count_candies > 0:
        if count_candies > 0:
            if whose_move == 'bot_login':
                count_candies -= bot_login(count_candies)
                print(f'Осталось конфет: {count_candies}')
                whose_move = 'user_login'

            elif whose_move == 'user_login':
                count_candies -= user_login()
                print(f'Осталось конфет: {count_candies}')
                whose_move = 'bot_login'

    print_winner(whose_move)