# Используем filter
# 2. Напишите программу, удаляющую из текста все слова, содержащие "абв".


with open('GB_Python_base/Py_Seminar/Seminar_005/Ex_data03.txt', 'rt') as inp_file:
    lst = list(inp_file.readline().split())

print(f'Слова в файле:  \n{lst}')

result = ' '.join(filter(lambda x: 'абв' not in x, lst)) # join обратно в строку
result2 = list(filter(lambda x: 'абв' not in x, lst))

print(f'Результат в файле:  \nв виде одной строки \n{result}, \nв виде lst \n{result2}')


#### второй вариант
# with open('l5_2.txt', 'rt') as inp_file:
#     array2 = list(inp_file.readline().split())
# print(array2)
# arr = filter(lambda x: 'abv' not in x.lower(), array2)
# print(*arr)