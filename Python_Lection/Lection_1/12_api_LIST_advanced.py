# Списки - расширенный функционал

colors = ['red', 'green', 'blue']

for i in colors:
 print(i) # red green blue

# индексом может быть любая буква например e
for e in colors:
 print(e*2) # redred greengreen blueblue

###функция append 
colors.append('gray') # добавить в конец
print(colors == ['red', 'green', 'blue', 'gray']) # True

print('-----')

#Удалить
colors.remove('red') #del colors[0] # удалить элемент
print(colors) #['green', 'blue', 'gray']

del colors[0]
print(colors) #['blue', 'gray']