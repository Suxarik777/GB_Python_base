# с клавиатоуры вводится даные
# в качестве разделителя добавить пробел

data = list(map(int, input('data: ').split()))
print(data)



# второй вариант без принудительного сохранения в list

data2 = map(int, input('data2: ').split())

for e in data2:
    print(e)

print('=======')

# и второй раз работать не будет!!!
for e in data2:
    print(e)

# результат работы map() это некий итератор по итератору можно 
# пробежаться только один раз, для того чтобы работать несколько 
# раз с одними и теми же значениеми полученными 
# в следствии работы функции map() 
# нужно их принудительно сохранить например list(map())

data3 = list(map(int, '1 2 3'.split()))
for e in data3:
    print(e)

print('=======')

# и при условии принудительного сохранения в list во время итерации map
# второй раз работает
for e in data3:
    print(e)