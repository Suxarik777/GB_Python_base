from welcom_rules import welcom
from whose_movie import random_movie

CANDIES = 2021


def start_system():
    count_candies = CANDIES
    welcom()
    whose_move = random_movie() # return 'user_login' && 'bot_login'

    while count_candies >= 0:



