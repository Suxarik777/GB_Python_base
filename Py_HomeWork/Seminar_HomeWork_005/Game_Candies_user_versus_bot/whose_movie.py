from random import randint


def random_movie():
    print('Итак давай выясним кто первый будет ходить?')
    input('Жми ENTER')
    random_roulette = randint(0, 1)
    if random_roulette == 0:
        print('Поздравляю! Твой ход первый!')
        return 'user_login'
    else:
        print('Можешь передохнуть, ход за ботом!')
        return 'bot_login'
