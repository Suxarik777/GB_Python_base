# Используем map
# 1. В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие
# A[i] - 1 = A[i-1]. Найдите это число.

# 

data = [5, 6, 7, 8, 9, 10, 12, 13]


for i in range(1, len(data) - 1):
    if data[i] - 1 != data[i-1]:
        print(data[i] - 1)



# второй вариант с интересным решением
with open('l5_1.txt', 'rt') as inp_file:
    array = list(map(int, inp_file.readline().split())) # запаковываме лист читая из файла строку интуя и добавляя пробел
print(array)

for i in range(len(array) - 1):
    if array[i] + 1 != array[i + 1]:
        print(array[i] + 1)