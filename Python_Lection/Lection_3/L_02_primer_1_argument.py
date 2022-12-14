# Анонимные, lambda функции
# пример кода

def calc(x):
    return x + 10

print(calc(10))

# представим что нужно решение теперь умножить на 10
# придется писать вторую функцию
def calc2(x):
    return x * 10

print(calc2(10))

# в итоге мы получим необходимость плодить много функций с одинаковой логикой

#######
## решение создать функцию: которая в качестве рагумента будет принимать операцию

def function_multiplication(x):
    return x * 10

def function_plus(x):
    return x + 10

print(calc(10))

def math(arguments_call_function_multiplication, x): # (операция, число)
    print(arguments_call_function_multiplication(x)) # вызываем функцию op (изначально аргумент операции) и передавать (число)

            # линейный код вызываем
math(function_multiplication, 10) # обрати внимание мы передаём параметром саму функцию, которая потом будет вызываться внутри функции
# и в данном случае мы отправляем аргументами фнкцию по перемножению на 10 и число которое требуется умножить

# хотим плюсануть и льправляем функцию по плюсованию на 10
math(function_plus, 10)