#Напишите программу, которая принимает на вход два числа и 
#проверяет, является ли одно число квадратом другого.

print('Задайте первое число: ')
first_number = int(input())

print('Задайте второе число: ')
second_number = int(input())

if first_number ** 2 == second_number:
    print(f'{first_number} является квадратом {second_number}')
elif second_number ** 2 == first_number:
    print(f'{second_number} является квадратом {first_number}')
else:
    print("ничего не квадратно)))")


### вариант два

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

if a**2 == b or b**2 == a:
    print('Yes')
else:
    print('No')