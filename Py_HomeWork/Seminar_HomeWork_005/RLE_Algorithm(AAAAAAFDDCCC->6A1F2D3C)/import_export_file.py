import os

os.chdir(os.path.dirname(__file__))

def import_string(file_name):
    with open(f'{file_name}', 'r', encoding='UTF-8') as file:
        while(line := file.readline().rstrip()):
            return line

        # for line in data:
        #     print(line.rstrip())

def export_string(file_name, string):
    with open(file_name, 'w', encoding='UTF-8') as file:
        file.write(string)
