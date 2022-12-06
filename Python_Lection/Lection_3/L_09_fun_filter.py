# Функция filter()
# (принмает функцию по которой делать отбор, сами данные)

data = [x for x in range(1, 10)]

# делаем выборку четных элементов

result = list(filter(lambda x: not x % 2, data))
print(result)