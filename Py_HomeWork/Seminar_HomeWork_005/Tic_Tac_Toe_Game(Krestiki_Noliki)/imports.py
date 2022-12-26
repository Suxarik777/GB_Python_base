import os


os.chdir(os.path.dirname(__file__))

# with open(filename) as file:
#     for line in file:
#         print(line.rstrip())

def view_playing_area(file_name):
    with open(f'{file_name}.txt', 'r', encoding='UTF-8') as file:
        while (line := file.readline().rstrip()):
            print(line)

# сбираем игровую площадку в лист в листе
def collect_array(file_name):
    with open(f'{file_name}.txt', 'r', encoding='UTF-8') as file:
        array = []
        while (line := file.readline().split()):    # собираем строку в массив
            array.append(line)
        # print(array)
        return array

# collect_array('enumerate_playing_area')