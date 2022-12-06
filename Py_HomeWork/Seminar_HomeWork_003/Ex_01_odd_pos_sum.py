# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


from random import randint


def odd_pos(lst):
    res = []
    for i in range(len(lst)): 
       if i % 2 != 0:
        res.append(lst[i])
    return res

len_lst = int(input('Задайте длину списка: '))
lst = [randint(1, 9) for i in range(len_lst)]

lst_odd_pos_num = odd_pos(lst)
result = sum(lst_odd_pos_num)

str_odd_pos_num = ''.join(str(lst_odd_pos_num).replace(',', ' и'))

print(f" - {lst} -> на нечётных позициях элементы {str_odd_pos_num}, ответ: {result}")