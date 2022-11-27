# 3 Задайте список из n чисел 
# последовательности (1 + 1 / n)**n и выведите на экран их сумму.

# *Пример:*

# - Для n = 6: [2.0, 2.25, 2.37, 2.44, 2.488, 2.52]     
# ->       14.072    (Округлять не обязательно)

import random

def fun_list_n_numbers(n):
    list_result = []
    for i in range(1, n + 1):
        formula_number = round((1 + 1 / i)**i, 3)
        list_result.append(formula_number)
        i += 1
    
    return list_result

def list_amount(list):
    result = float()
    for i in list:
        result += i
    return result



user_n = int(input('Введите число N: '))

numbers_list = fun_list_n_numbers(user_n)
print(numbers_list)

amount_numbers = list_amount(numbers_list)
print(amount_numbers)