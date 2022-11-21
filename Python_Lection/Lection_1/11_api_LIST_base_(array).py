# Списки - базовый функционал

numbers = [1, 2, 3, 4, 5]
print(numbers) # [1, 2, 3, 4, 5]


######## ранжируем
# если просто задаём ранжирование без создания списка
ran = range(1,6)
print(type(ran)) # получаем тип данных range (а нам нужен тип даных list)

# приводим тип данных range к типу данных list
numbers = list(range(1, 6)) 
print(type(numbers))
print(numbers) # [1, 2, 3, 4, 5]


numbers[0] = 10 # записать в 0 элемент списка число 10

print(len(numbers)) # длина списка - 5

print(numbers) # [10, 2, 3, 4, 5]

print()
print('цикл for')

for i in numbers:
 i *= 2 # это значит что в текущую переменую кладём значение (но потом её затрём)
 print(i) # [20, 4, 6, 8, 10]
# сам список не тронут!
print(numbers) # [10, 2, 3, 4, 5]