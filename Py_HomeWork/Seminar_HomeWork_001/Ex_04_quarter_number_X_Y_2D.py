# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат 
# точек в этой четверти (x и y).

quarter_number = int(input('Введите номер четверти: '))

if quarter_number > 0 and quarter_number < 5:
    if quarter_number == 1: print('x = 1 -> oo \ny = 1 -> oo')
    elif quarter_number == 2: print('x = -oo -> -1 \ny = 1 -> oo')
    elif quarter_number == 3: print('x = -oo -> -1 \ny = -oo -> -1')
    elif quarter_number == 4: print('x = 1 -> oo \ny = -oo -> -1')
else: print('Такой четверти нет в координатах x, y - нет')