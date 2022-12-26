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