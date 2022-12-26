# 4 Задана натуральная степень k. Сформировать случайным образом 
# список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.

# *Пример:* 

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0



import random
import os

os.chdir(os.path.dirname(__file__))

def write_file(string):
    with open('Ex_04.txt', 'w') as data:
        data.write(string)


def random_fun():
    return random.randint(0, 101)


def create_mn(k):
    lst = [random_fun() for i in range(k + 1)]
    return lst


def create_str(step_k):
    lst = step_k[::-1]
    line_string = ''
    if len(lst) < 1:
        line_string = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                line_string += f'{lst[i]}x^{len(lst)-i-1}'
                if lst[i+1] != 0:
                    line_string += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                line_string += f'{lst[i]}x'
                if lst[i+1] != 0:
                    line_string += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                line_string += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                line_string += ' = 0'
    return line_string


k = int(input("Введите натуральную степень k = "))
koef = create_mn(k)
write_file(create_str(koef))