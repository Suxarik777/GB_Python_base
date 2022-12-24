# 1. Напишите программу вычисления арифметического выражения заданного строкой.
#    Используйте операции +,-,/,*. приоритет операций стандартный.

#     *Пример:*

#     2+2 => 4;
#     7-8+3*5+1+1+2*3 => 22;

# a = '7-82+3*5+13+1+25*3'

# b = ['7', '-', '82', '+', '3', '*', '5', '+', '13', '+', '1', '+', '25', '*', '3']

#     7, -8, 15, 1, 1, 6


#     1-2*3 => -5;


def pars_str_in_lst(str):
    str = str.replace('+', ' + ')
    str = str.replace('*', ' * ')
    str = str.replace('-', ' - ')
    str = str.replace('/', ' / ')
    return str.split()

def calc_parse(digit_lst):
    new_list = []
    for i in range(len(digit_lst)):
        if digit_lst[i].isdigit() and i > 0:
            digit_lst[i] = float(digit_lst[i])
            if digit_lst[i-1] == '+':
                new_list.append(digit_lst[i])
            elif digit_lst[i-1] == '-':
                new_list.append(digit_lst[i] * -1)
            elif digit_lst[i-1] == '*':  # если предыдущий элемент от i
                new_list[-1] = new_list[-1] * digit_lst[i] # перезаписываем элемент последний i текущий на последний (он раньше) 
            elif digit_lst[i-1] == '/':
                new_list[-1] = new_list[-1] / digit_lst[i]
        elif digit_lst[i].isdigit() and i == 0: # отрабатывает первый элемент массива
            digit_lst[i] = float(digit_lst[i])
            new_list.append(digit_lst[i])
    return sum(new_list)


string = '7-8+3*5+1+1+23*3'
print(string)

digit_lst = pars_str_in_lst(string)
res = calc_parse(digit_lst)
print(res)