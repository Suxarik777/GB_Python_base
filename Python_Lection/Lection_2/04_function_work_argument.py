def new_string(symbol, count):
    return symbol * count # вспоминаем что python умеет перемножать символы


print(new_string('!', 5)) # !!!!!
print(new_string('!')) # TypeError missing 1 required ...


# можем заранее указать значение аргумента, если в него ничего не приходит

def new_string2(symbol, count = 3):
    return symbol * count 


print(new_string2('!', 5)) # !!!!!
print(new_string2('!')) # !!!

# и вспоминаем о динамической типизации, если отправим число то получим 
# обычное умножение
print(new_string2(4)) # 12


##########
## неограниченное количество аргументов

def concatenatio(*params):
    res: str = "" # создание переменной с обязательным присвоение типа данных
    for i in params:
        res += i
    return res


print(concatenatio('a', 's', 'd', 'w')) # asdw
print(concatenatio('a', '1', 'd', '2')) # a1d2
# print(conatenatio(1, 2, 3, 4)) # TypeError: ...

# соответсвенно чтобы заработало с цифрами нужно изменить в функции 
# обязательное присвоение на int

def concatenatio2(*params):
    res: int = 0 # создание переменной с обязательным присвоение типа данных
    for i in params:
        res += i
    return res

print(concatenatio2(1, 2, 3, 4))