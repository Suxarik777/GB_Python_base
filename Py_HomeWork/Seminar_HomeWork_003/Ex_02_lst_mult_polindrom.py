# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


from random import randint

def mult_pairs_num(lst):
    i = 0
    res = []

    if len(lst) % 2 == 0:
        while i != len_lst // 2:
            res.append(lst[i] * lst[len(lst) - 1 - i])
            i += 1
    else:
        while i != len_lst // 2:
            res.append(lst[i] * lst[len(lst) - 1 - i])
            count = i + 1
            i += 1
        res.append(lst[count] * lst[count])

    return res


len_lst = int(input('Задайте длину списка: '))

lst = [randint(1,9) for i in range(len_lst)]
lst_result = mult_pairs_num(lst)

print(f'{lst} => {lst_result}')