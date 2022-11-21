# Управляющие конструкции
# if, if-else

a = int(input('a = '))
b = int(input('b = '))

if a > b:
    print(a)
else:
    print(b)


#####
username = input('Введите имя: ')

if username == 'Маша':
    print('Ура, это же МАША!')
elif username == 'Марина':
    print('Я так ждала Вас, Марина')
elif username == 'Ильнар':
    print('Ильнар - топ')
else:
    print('Привет, ', username)