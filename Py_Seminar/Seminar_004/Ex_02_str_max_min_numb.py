# 1. Задайте строку из набора чисел. Напишите программу,
#     которая покажет большее и меньшее число.
#     В качестве символа-разделителя используйте пробел.


test_list = []

for i in input("Введите числа через пробел: ").split():
    test_list.append(int(i))

print(min(test_list))
print(max(test_list))

# или идем через if

max_num = 0
min_num = 0

for i in test_list:
    if i > max_num:
        max_num = i
    if i > min_num:
        min_num = i

print(max_num, min_num)