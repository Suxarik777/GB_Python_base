def check_game(arr_game):
    # count_1 = 0
    # count_2 = 0
    # count_3 = 0
    # for line in arr_game:
    #     for i_row in line:
    #         if i_row == '+':
    #             count_1 += 1
    #         if i_row == '0':
    #             count_2 += 1
    # if count_1 >=3 and count_2 >=2:

    if (arr_game[0][0] == arr_game[0][2] == arr_game[0][4] or  # проверка по строкам
            arr_game[2][0] == arr_game[2][2] == arr_game[2][4] or
            arr_game[4][0] == arr_game[4][2] == arr_game[4][4] or
            arr_game[0][0] == arr_game[2][0] == arr_game[4][0] or  # проверка по линиям
            arr_game[0][2] == arr_game[2][2] == arr_game[4][2] or
            arr_game[0][4] == arr_game[2][4] == arr_game[4][4] or
            arr_game[0][0] == arr_game[2][2] == arr_game[4][4] or  # проверка наискосок
            arr_game[0][4] == arr_game[2][2] == arr_game[4][0]):
        return 'stop_game'
    else:
        chek_str = 0
        for line in arr_game:
            for i_row in line:
                if i_row in {'1', '2', '3', '4', '5', '6', '7', '8', '9'}:
                    chek_str += 1
        if chek_str >= 1:
            return 'game'
        else:
            return 'game_over'


def swich_game_click(who_gamer):
    if who_gamer == 'user_1':
        return 'user_2'
    else:
        return 'user_1'

def check_user_input_pos(i_line, i_row, arr_game):
    if arr_game[i_line][i_row] in {'+', '-'}:
        return False
    else:
        return True




# test = [['1', '|', '2', '|', '3'], ['-----------'], ['4', '|', '5', '|', '6'], ['-----------'], ['7', '|', '8', '|', '9']]
#
# check_game(test)
