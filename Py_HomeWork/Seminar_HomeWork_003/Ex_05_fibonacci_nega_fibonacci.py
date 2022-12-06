# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fib(num):
    if num in [1, 2]:                       
        return 1
    else:
        return fib(num-1) + fib(num-2)

def nega_fib(num):
    if num == 1:                       
        return 1
    elif num == 2:                       
        return -1
    else:
        number1, number2 = 1, -1
        for i in range(2, num):
            number1, number2 = number2, number1 - number2
        return number2

list = []
number = int(input('Введите число фибоначи: '))
for i in range(1, number + 1):
    list.append(fib(i))
    list.insert(0, nega_fib(i))
print(list)