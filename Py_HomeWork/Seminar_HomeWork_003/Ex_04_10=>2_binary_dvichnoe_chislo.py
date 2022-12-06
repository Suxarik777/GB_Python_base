# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

num = int(input('Введите число: '))

binary_number = []

while num > 0:
    binary_number.append(str(num % 2))
    num //= 2

binary_number = ''.join(binary_number[::-1])
print(binary_number)