# Множества
# set

colors = {'red', 'green', 'blue'}
print(colors) # {'red', 'green', 'blue'}


### Добавление .add
colors.add('red')
print(colors) # {'red', 'green', 'blue'}
colors.add('gray')
print(colors) # {'red', 'green', 'blue','gray'}

### Удаление .remove
colors.remove('red')
print(colors) # {'green', 'blue','gray'}
# colors.remove('red') # KeyError: 'red' # если элемента уже нет

## удаление элемента без ошибки если его нет
colors.discard('red') # ok

print(colors) # {'green', 'blue','gray'}

#### Очистка множества
colors.clear() # { }
print(colors) # set()