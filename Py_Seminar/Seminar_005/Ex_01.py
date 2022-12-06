list = [(1, 8), (6,2), (4,2), (6,1)]

print(max(lst, key=lambda x: x(1))) # ищем второй элемент в картеже



a, b, c = map(int, input().split())
print(a, b, c)


item = lst(map(int, input().split()))
print(item)

print(*item)



# как перевести двоичную в 10
a = int('101', 2)


# filter
lst = [2, 33, 12, 34, 3, 13]

# отсеиваем не четные числа
a = filter(lambda x: not x%2, lst)
print(*a)

for index, x in enumerate(lst): #получаем и индекс и значение
    print(index, x)

# либо сразу кортежем
for tupe in enumerate(lst): #получаем и индекс и значение
    print(tupe)

# List comprehension
lst = []

for x in range(-2, 7):
    if x%2==0:
        lst.append(x*x)
    else:
        lst.append(x * x * x)

# то что выше можно записать сразу так:
lst1 = [x*x for x in range(-2,7) if x%2==0]

# если условия два что либо так либо else то условия пишутся вперёд
lst1 = [x*x if x%2==0 else x * x * x for x in range(-2,7)]

