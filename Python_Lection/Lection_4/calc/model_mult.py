# модуля посчитать умножение двух значений

x = 0
y = 0

def init(a, b):
    global x # делает переменную глобальной и видимой не только в функции
    global y
    x = a
    y = b

def do_it():
    return x * y