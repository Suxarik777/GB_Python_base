# выведите кортежем (четное число, это же число в квадрате)

# def select_list(fun, col):       
#     return [fun(x) for x in col]
# ####
###### благодаря map() функция select_list не нужна


# функция создающая условия по которым нужно произвести фильтрацию объетов
# [условие, непосредственно данные]
# def where (fun, col):
#     return [x for x in col if fun(x)]
###### благодаря flter() функция where не нужна


data2 = '1 2 3 5 8 15 23 38'.split() # метод сплит превратит ['1', '2', '3', '5'.....]

# result = select_list(int, data2) # генереруем списко из data превращая его в числа
result = map(int, data2) # интерируй данные (в число int, из файла data)


# result2 = where(lambda x: not x%2, result) # отправляем четные числа и сгенерированный список
result2 = list(filter(lambda x: not x%2, result))



result3 = list(map(lambda x: (x, x**2), result2))
            # запиши данные в list попутно интерируя их (число x в кваодрат, из ранее интерируемого result)

print(result)
print(result2)
print(result3)