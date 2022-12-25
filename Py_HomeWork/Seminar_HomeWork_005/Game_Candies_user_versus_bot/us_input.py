

def user_login(min_eat_candies=1, max_eat_candies=28):
    user_digit = int(input(f'ТВОЙ ХОД!: \nВведите число от {min_eat_candies} до {max_eat_candies}: '))
    if min_eat_candies <= user_digit <= max_eat_candies:
        return user_digit
    else:
        print("УПС! Вы ввели что-то не то")
        return user_login()


