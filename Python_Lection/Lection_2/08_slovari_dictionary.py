# Работа со словарём

dictionary = {} # создаём пустой словарь кладём в переменную

# присваеваем значения чтоб их вызывать

                # обратный слэш позволяет не писать всё в одну строку
dictionary = \
    {
        'up': '↑', # 'ключь или наименование вызова', 'что будет прилетать'
        'left': '←',
        'down': '↓',
        'right': '→'
    }

# иначе dictionary = {'up': '↑', 'left': '←' ...}

# показать полностью словарь
print(dictionary)

# вызвать элемент по присвоеному названию
print(dictionary['up']) # ↑  
        # обрати внимание что в ''

########
### показать ключи коллекция .keys()

for k in dictionary.keys():
    print(k)

#####
### показать значения коллекции .values()
for k in dictionary.values():
    print(k)

#####
### иной показ ключей и значений словаря

for k in dictionary:
    print(k, end=': ') # видим ключи
    print(dictionary[k]) # видим значения

for i in dictionary: # for (k,v) in dictionary.items():
    print(f'{i}: {dictionary[i]}') # print('{}: {}'.format(item, dictionary[item]))
# up: ↑
# down: ↓
# right: →


########
### Замена элемента по ключу и удаление
dictionary['left'] = '⇐'
print(dictionary['left']) # ⇐
#print(dictionary['type']) # KeyError: 'type' -> нет такого ключа
del dictionary['left'] # удаление элемента
