#2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
    
#   Примеры:
    
#    - 1, 4, 8, 7, 5 -> 8
#    - 78, 55, 36, 90, 2 -> 90

a = int (input("введите a: "))
b = int (input("введите b: "))
c = int (input("введите c: "))
d = int (input("введите d: "))
e = int (input("введите e: "))

max_number = a

for i in a, b, c, d, e:
    if i > max_number: max_number = i

print(f"максимальное число {max_number}")



#list.append(переменная) - положить эту переменную в список

max_number = float('-inf')

for i in range(1, 6):
    number = int(input(f'Введите число {i}: '))
    if number > max_number:
        max_number = number

print(max_number)