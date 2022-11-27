# 1 Напишите программу, которая принимает на вход 
# вещественное число и показывает сумму его цифр.

# *Пример:*

# - 6782 -> 23
# - 0.56 -> 11


user_numb = (input('Введите число: '))

inter_result = user_numb.replace('.', '')
result = int()

for i in range(len(inter_result)):
    result += int(inter_result[i])

print(result)
