text = 'съешь ещё этих мягких французских булок'

# вызов длины текста
# print(len(text)) # 39

# слово есть в тексте?
# print('ещё' in text) # True

# переменная text числовая?
# print(text.isdigit()) # False

# все символы строки в нижнем регистре?
# print(text.islower()) # True

# заменить слово на слово
# print(text.replace('ещё','ЕЩЁ')) #


#######
# обращение к функции если забыл что она делает
#help(text.replace)
########


text = 'съешь ещё этих мягких французских булок'
# вспоминаем строка это как массив данных

print(text[0]) # c
print(text[1]) # ъ

print(text[len(text)]) # IndexEror потому что индексация начинается с 0
print(text[len(text)-1]) # к - поэтому последняя буква -1

print(text[-5]) # б - можно не писать большую абревиатуру и просто поставить - тогда подсчёт с конца


# вывод текста от символа до символа
print(text[:]) # print(text)
# по умолчанию подставляет от первого до последнего элемента
# print(text[0 : len(text) - 1])

print(text[:2]) # съ
# как будто от text[0:2] - от 0 символа до второго

########
# считаем конец строки
print(text[len(text)-2:]) # ок
# длина строки от -2 символа до конца

# при этом можно просто поставить отрицательное цисло тогда это будет 18 символ от конца
print(text[6:-18]) # ещё этих мягких

print(text[2:9]) # ешь ещё

# [от : до : шаг через которой брать селд элемент]
print(text[0:len(text):6]) # сеикакл
print(text[::6]) # сеикакл


text = text[2:9] + text[-5] + text[:2] # ...