# Ввод данных и их преобразование

# print() - вывод данных

# input() - ввод данных

print('Введите a')
a = input()
print('Введите b')
b = input()

print(a, b)
print('{} {}'.format(a, b))
print(f'{a} {b}')

# типизация в python динамическая и мы не задаём заранее тип данных

# по умолчанию ввод данных str (строки)
print('Введите a')
a = input()
print('Введите b')
b = input()

print(a, ' + ', b, ' = ', a+b) # и мы получим два сложенных числа

# принудительное присваивание типа данных
print('Введите a')
a = int(input())
print('Введите b')
b = int(input())

print(a, ' + ', b, ' = ', a+b) # и мы получим два сложенных числа