import os


os.chdir(os.path.dirname(__file__))

# arr = [['1', '|', '2', '|', '3'], ['-----------'], ['4', '|', '5', '|', '6'], ['-----------'], ['7', '|', '8', '|', '9']]


def update_arr(i_line, i_row, symbol, array):
    del array[i_line][i_row]
    array[i_line].insert(i_row, symbol)
    return array



# update_arr(2, 0, '+', arr)