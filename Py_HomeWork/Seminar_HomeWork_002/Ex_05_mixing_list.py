# 5 Реализуйте алгоритм перемешивания списка.
# Из библиотеки random использовать можно только randint

import random

def input_list_in_order(length):
    i = 0
    list = []
    while i < length:
        list.append(i + 1)
        i += 1
    return list

def list_mixing(list):
    i = 0
    while i < len(list):
        help_pos = random.randint(0, len(list) - 1)
        help = list[i]
        list[i] = list[help_pos]
        list[help_pos] = help
        i += 1
    return list


user_len_list = int(input('Введите длину списка: '))
list = input_list_in_order(user_len_list)

print(list)

list_mix = list_mixing(list)
print(list_mix)