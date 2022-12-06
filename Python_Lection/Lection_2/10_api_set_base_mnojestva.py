# Продолжаем множество API base

a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}

# Скопировать множество
c = a.copy() # c = {1, 2, 3, 5, 8}

# Объединение множеств (числа не повторяются)
u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21}

# Вывод повторяющихся (пересекающихся) значений в множестве a
ia = a.intersection(b) # i = {8, 2, 5}
ib = b.intersection(a) # i = {2, 5, 8}

# Вывод  не повторяющихся (пересекающихся) значений в множестве
dl = a.difference(b) # dl = {1, 3}
dr = b.difference(a) # dr = {13, 21}


# вспомниаем обратны \ позволяет код переносить на новую строку
q = a \
    .union(b) \
    .difference(a.intersection(b))
# {1, 21, 3, 13}

# создание неизменяемого множества
s = frozenset(a) # замороженное сножество
# методы добавления или удаления работать не будут

a = {1, 2, 3, 5, 8}
b = frozenset(a)
print(b) # frozenset({1, 2, 3, 5, 8})