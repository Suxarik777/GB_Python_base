# 2 Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N.

# (факториал)

# *Пример:*

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


def fun_factorial(len_numbers):
    result_list = []
    factorial = int(1)
    for i in range(1, len_numbers + 1):
        factorial *= i
        result_list.append(factorial)
    return result_list

user_n = int(input('Введите число N: '))
result_list = fun_factorial(user_n)

print(result_list)