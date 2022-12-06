
# 3. Задайте два числа. Напишите программу, которая найдёт НОК
#    (наименьшее общее кратное) этих двух чисел.


dividing_list = []

for i in input("Введите числа через пробел: ").split():
    dividing_list.append(int(i))

product = dividing_list[0] * dividing_list[2]
list1 =[]
list2 = []

for i in range(dividing_list[0], product + 1, dividing_list[0]):
    list1.append(i)

for j in range(dividing_list[1], product + 1, dividing_list[1]):
    list2.append(j)

list3 = []

for k in list1:
    for l in list2:
        if k == l:
           list3.append(k)

print(list1)
print(list2)
print(list3[0])


