import os

if __name__


# полный путь до данного файла
print(__file__)

# путь до папки
print(os.path.dirname(__file__))

#исправление нахождение файла на создание относительно файла main (рядом)
os.chdir(os.path.dirname(__file__))


# Создать калькулятор для работы с рациональными и комплексными числами, организовать меню, 
#    добавив в неё систему логирования.

# В рамках этого обсуждения студентам надо нарисовать “архитектуру” 
#      (например, в виде блок-схемы) для работы данного приложения.

print(complex('12+6j')) # комплексное число

b = complex('12+6j')

print(type(b))


# b = complex('12+6j') * complex('5+3j')

# print(b)  # (42+66j)

# b = complex('12+6j') + 66

# print(b)  # (78+6j)

# https://www.webmath.ru/poleznoe/formules_16_9.php


# functions.py - вычисления
# input_number.py - ввод # input_c
# output_number.py - вывод
# controller.py
# main.py



Домашка
operations = {'+': lambda x, y: x + y,
              '-': lambda x, y: x - y,
              '*': lambda x, y: x * y,
              '/': lambda x, y: x / y}

op = '+'
n1, n2 = 25, 6

print(operations[op](n1, n2))