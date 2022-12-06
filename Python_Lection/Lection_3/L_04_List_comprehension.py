# Создай четный список от 1 до 100

list_us = []

for i in range(1, 101):
    if(i%2 == 0):
        list_us.append(i)

print(list_us)

print('=============')

# но можно запихнуть это всё сразу при создании list

list_us2 = [k for k in range(1, 21)] # запиши k, которая пробежится по циклу for по range
print(list_us2)

# добавим условие записи только четных
list_us3 = [j for j in range(1, 21) if j%2 == 0]
print(list_us3)

# делаем кортежи (tuple) из двух чисел
list_us4 = [(i, i) for i in range(1, 21) if i%2 == 0]
print(list_us4)

###########
# также мы можем обрабатывать данные при записи листа

def f(x):
    return x**3

list_us5 = [f(i) for i in range(1, 21) if i%2 == 0]
print(list_us5)

# сделаем нагляднее через tuple - кортежи
list_us6 = [(i, f(i)) for i in range(1, 21) if i%2 == 0] # выводим число и его куб через функцию
print(list_us6)

