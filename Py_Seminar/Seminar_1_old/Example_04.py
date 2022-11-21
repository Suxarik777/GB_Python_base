# 1. Напишите программу, которая будет на вход 
# принимать число N и выводить числа от -N до N
    
#     *Примеры:* 
    
#     - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5


# input_n = int(input("Введите N "))

# if input_n < 0: n = -input_n

# else: n = input_n

# for i in range(-n,n+1):
#     print(f"{i} ", end='')



print('введите числа')

value = int(input())

print (list (range(-value, value+1)))