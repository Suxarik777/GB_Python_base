# ввод данных в строку


# def input_c():
#     user_input = input('Введите пример по типу 1 + 1: ')
#     arr = user_input.split()
#     return arr



# этот вариант позволит рациональные числа принимать
def input_c():
    lst = []
    digit_count = 1
    # how_num = 2
    for i in range(3):
        if i % 2 != 0:
            user_input = input('sign: ')
            lst.append(user_input)
        else:
            user_input = input(f'value {digit_count}: ')
            lst.append(user_input)
            digit_count += 1
    
    return lst

def output_c(result):
    print(f'Result: {result}')