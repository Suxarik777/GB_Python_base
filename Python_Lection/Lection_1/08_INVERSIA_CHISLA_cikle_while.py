# цикл while

original = 23
inverted = 0

while original !=0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
print(inverted)


# к циклу while можно добавить блок else когда цикл закончит своё действие
original = 23
inverted = 0

while original !=0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
    #print(original)
else:
    print('Пожалуй')
    print('хватит )')
print(inverted)