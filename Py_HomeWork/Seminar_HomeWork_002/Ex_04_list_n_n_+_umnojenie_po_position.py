# 4 Задайте список из N элементов, 
# заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции вводятся с клавиатуры.

def filling_list(n):
    result_list = []
    for i in range(-n, n+1):
        result_list.append(i)
    return result_list

def mult_pos_in_list(list, pos1, pos2):
    result = list[pos1] * list[pos2]
    return result

user_n = int(input('Введите число N: '))
user_pos1 = int(input('Введите позицию 1: '))
user_pos2 = int(input('Введите позицию 2: '))

list_n_n = filling_list(user_n)
print(list_n_n)

sum_pos = mult_pos_in_list(list_n_n, user_pos1, user_pos2)
print(f'{list_n_n[user_pos1]} * {list_n_n[user_pos2]} = {sum_pos}')