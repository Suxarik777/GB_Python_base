# Анонимные, lambda функции

def function(x):
    x**2

lambda_function = function # в новую переменную кладём функцию

print(type(function))

print(function(1))
print(lambda_function(1)) # и получается что мы функции даём второе название


# ещё раз

def function(x):
    return x**2

print(function(2))

print(type(function)) # так смотрим какой тип данных у функции
print(type(function(2))) # если добавляем параметр функции, то получаем какой тип данных она возвращает

# у функции есть тип а значит функцию как единицу можно положить в переменую

copy_function = function # обрати внимание не передаём параметры функции
print(function(2))
print(copy_function(2))