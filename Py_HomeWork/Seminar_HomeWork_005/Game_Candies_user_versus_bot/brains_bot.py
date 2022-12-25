from random import randint


def bot_login(count_candies, max_eat_candies=28):
    if count_candies <= max_eat_candies:
        print(f'Кушаю все {count_candies} конфеты')
        return count_candies
    elif count_candies == max_eat_candies + 2:
        print(f'Вот ты и попался)) Скушаю-ка я всего одну штучку')
        return 1
    elif count_candies == max_eat_candies * 2:
        help_res = max_eat_candies - 2
        print(f'Всё равно победа будет за мной! Я съем  {help_res} кофеты')
        return help_res
    elif count_candies < max_eat_candies * 2:
        count = 0
        while count_candies != max_eat_candies + 1:
            count_candies -= 1
            count +=1
        help_res = count
        print(f'Я тебя побеждаю! Я съем  {help_res} кофеты')
        return help_res
    else:
        help_res = randint(1, max_eat_candies)
        print(f'Я ем {help_res} кофеты')
        return help_res

