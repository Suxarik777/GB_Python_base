# 3 Задайте последовательность чисел. Напишите программу, которая 
# выведет список неповторяющихся элементов исходной последовательности.

# *Пример*

# - при [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]     ->        [2, 4, 5, 9]



from random import randint
import math

lst_mult = [randint(1,1000) for x in range(randint(1, 5))]
print(lst_mult)


lst_mult2 = math.prod(lst_mult)
print(lst_mult2)