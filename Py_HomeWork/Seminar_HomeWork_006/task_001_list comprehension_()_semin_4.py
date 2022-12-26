# 2 Задайте натуральное число N. Напишите программу, которая составит
# список простых множителей числа N.

# *Пример*

# - при N=236     ->        [2, 2, 59]



def list_mult(n):
    lst = []
    listMult = [lst.append(i) for i in range(1, n+1) if n % i == 0]
    return lst
#Расклад числа на множители => [1, 2, 4, 5, 10, 20, 25, 50, 100]

def digit_mult(n):
    res_lst = []
    for i in range(2, n):
        while n % i == 0:
            n /= i
            res_lst.append(i)
    return res_lst


user_n = int(input('Задайте число N: '))

mult_num_from_user_n = list_mult(user_n)
simple_mult_num_from_user_n = digit_mult(user_n)

print(f'''---------------------------
Множители числа {user_n}: 
{mult_num_from_user_n}
---------------------------
Простые множетели числа {user_n}
{simple_mult_num_from_user_n}''')