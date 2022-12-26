# 3 Задайте последовательность чисел. Напишите программу, которая
# выведет список неповторяющихся элементов исходной последовательности.

# *Пример*

# - при [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]     ->        [2, 4, 5, 9]



from random import randint
import math


lst = [randint(1, 10) for x in range(1, 10)]
print(lst)

# проверяет каждый новый элемент, который ранее не появлялся в списке, прежде чем добавлять его
result = [ii for n, ii in enumerate(lst) if ii not in lst[:n]]
print(result)