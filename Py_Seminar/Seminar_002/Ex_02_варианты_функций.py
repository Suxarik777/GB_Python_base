# Функции

# функция квадратного корня

def function(number):
    print(number ** 0.5)

function(36)


def function(number):
    return n = number ** 0.5

number = function(36)
print(number)


# как заблокировать вывод по типу данных

lst = []
 
 
def add_to_lst(item):
    if isinstance(item, int):
        lst.append(item)
 
 
add_to_lst(66)
add_to_lst('ww')
add_to_lst(65.5)
add_to_lst(2)
add_to_lst(None)
print(lst)
