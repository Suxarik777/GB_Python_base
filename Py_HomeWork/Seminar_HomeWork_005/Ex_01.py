# 1  Напишите программу, удаляющую из файла все слова, содержащие "абв"


import os

os.chdir(os.path.dirname(__file__))

with open('Ex_01_text_file.txt', 'rt') as data:
    lst = list(data.readline().split())


print(f'Слова в файле:  \n{lst}')
print('Слова в файле в виде строки: \n', ' '.join(lst))

result_lst = list(filter(lambda x: 'абв' not in x, lst))

print('Итоговый результат: \n', result_lst)
print(f'Итоговый результат в виде строки: \n', ' '.join(result_lst))

with open('Ex_01_text_file.txt', 'a') as input_str:
    result_str = ' '.join(result_lst)
    input_str.writelines(f'\n {result_str}')



# with open('GB_Python_base/Py_Seminar/Seminar_005/Ex_data03.txt', 'rt') as inp_file:
#  lst = list(inp_file.readline().split())
#
# print(f'Слова в файле:  \n{lst}')
#
# result = ' '.join(filter(lambda x: 'абв' not in x, lst))  # join обратно в строку
# result2 = list(filter(lambda x: 'абв' not in x, lst))
#
# print(f'Результат в файле:  \nв виде одной строки \n{result}, \nв виде lst \n{result2}')
