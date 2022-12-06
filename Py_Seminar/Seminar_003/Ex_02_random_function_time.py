from time import time

print(time())

# это время с 1 января 1970 года количество секунд с этой даты, хранится в 
# вещественных числах


# 1. Реализуйте алгоритм задания случайных чисел без использования 
#    встроенного 
#    генератора псевдослучайных чисел.


num = time() % 1 * 1000
print(round(num))



# from time import time

# def randfromtime(max):
#     time1 = time()
#     time1 = (time1 - int(time1))
#     return int(time1 * max)

# print(randfromtime(1000))