# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и
# минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


from random import uniform

def max_min_after_dot_num(lst):
    help = []
    for i in lst:
        help.append(int(i % 1 * 100))

    result = max(help) - min(help)
    return result


len_lst = 5
float_lst = [round(uniform(1, 11), 2) for i in range(len_lst)]

res = max_min_after_dot_num(float_lst)

print(f'{float_lst} => 0.{res}')