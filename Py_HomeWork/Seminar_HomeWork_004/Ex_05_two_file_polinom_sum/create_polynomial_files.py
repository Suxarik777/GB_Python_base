import os


os.chdir(os.path.dirname(__file__))

polynom_1_str = '7x ^ 6-29x ^ 5-54x ^ 4-86x ^ 3 + 74x ^ 2-32x + 27 = 0'
polynom_2_str = '-9x ^ 6 + 87x ^ 5 + 45x ^ 4-29x ^ 3-44x ^ 2 + 78x + 40 = 0'

def before_start():
    with open('polynom_1.txt', 'w', encoding='utf-8') as file:
        file.write(polynom_1_str)
    with open('polynom_2.txt', 'w', encoding='utf-8') as file:
        file.write(polynom_2_str)

before_start()