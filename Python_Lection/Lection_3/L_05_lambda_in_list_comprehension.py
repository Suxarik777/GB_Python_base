# К чему это всё?
# В файле хранятся числа, нужно выбрать четные и
# составить список пар (число; квадрат числа).
# Пример:
# 1 2 3 5 8 15 23 38
# Получить:
# [(2, 4), (8, 64), (38, 1444)]


path = '/Users/aleksandrgultcev/Documents/Taining_in_GB/GB_Python_base/Python_Lection/Lection_3/L_05_xfile.txt'
file = open(path, 'r')
data = file.read() + ' ' # записали в переменую data данные с файла
file.close

numbers = []

while data != '': #пока моя строка не пустая
    space_pos = data.index(' ') # находим первую позицию пробела
    numbers.append(int(data[:space_pos])) # срез от первого символа до пробела
    data = data[space_pos+1:] #перезапись data с помощью среза для работы после пробела

out = []
for e in numbers:
    if not e % 2:
        out.append((e, e**2))
print(out)

print("===========================")

# list_file = [1, 2, 3, 5, 8, 15, 23, 38]

# # list_intermed = [input(lambda list_file: )]
# def calc(op, n):
#     return op(n)

# lis_result = [(i, j) for i in list_file if i%2==0 for j in list_file if j%2==0]

########
### применяем полученые знания


# превый аргумент [функция отвечающая за логику обработки, данные которые во втором аргументе]
# (иными словами обрабатываем данные по нужным параметрам)
def select_list(fun, col):       
    return [fun(x) for x in col]


# функция создающая условия по которым нужно произвести фильтрацию объетов
# [условие, непосредственно данные]
def where (fun, col):
    return [x for x in col if fun(x)]

data2 = '1 2 3 5 8 15 23 38'.split() # метод сплит превратит ['1', '2', '3', '5'.....]

result = select_list(int, data2) # генереруем списко из data превращая его в числа
result2 = where(lambda x: not x%2, result) # отправляем четные числа и сгенерированный список
result3 = select_list(lambda x: (x, x**2), result2)

print(result)
print(result2)
print(result3)


