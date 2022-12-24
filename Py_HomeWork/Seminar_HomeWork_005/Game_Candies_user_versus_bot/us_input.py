

def user_input():
    user_digit = int(input('Введите число от 1 до 28: '))
    if user_digit.isdigit() and 1 <= user_digit <= 28:
        return user_digit
    else:
        print("УПС! Вы ввели что-то не то")
        return user_input()


