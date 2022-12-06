# 2. Задайте список. Напишите программу, которая определит, 
# присутствует ли в 
#    заданном списке строк некое число.
#    ['22', '33', '123', 'fwefe', 'ytyy', '55']
   
#    f(n)


num = int(input('Введите число: '))

test_list = ['22', '33', '123', 'fwefe', 'ytyy', '55']

str_num = str(num)

def Search_Number(list_1, str_num: str):
    for i in range(0, len(list_1)):
        if str_num == list_1[i]:
            return True, i


a = Search_Number(test_list, str_num)
if a[0] == True: 
    print(f"{str_num} присутствует в списке под индексом {a[1]}")
else: 
    print(f"Заданное число не присутствует в списке")