# распаковка списка -> кортежа - в отдельные переменные


spisok = ['red', 'green', 'blue'] # ессть список
t = tuple(spisok) # преобразование в кортеж
red, green, blue = t # выводим значение в кортеже(списке) в самостоятельные переменные

# и далее мы можем с ними работать как с обычными переменными
print('r:{} g:{} b:{}'.format(red, green, blue))
# или
print(f'r: {red} g: {green} b: {blue}')

# попробуем в них что то поменять
red = 'reding'
green = "GGGG"
blue = 123
print(f'r: {red} g: {green} b: {blue}')