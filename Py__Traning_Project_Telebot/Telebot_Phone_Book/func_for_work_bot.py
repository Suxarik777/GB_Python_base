import os
import csv


os.chdir(os.path.dirname(__file__))

def read_file():
    with open('inputs.csv', 'r', encoding='utf-8') as csvfile:
        file_reader = csv.reader(csvfile, delimiter=';', skipinitialspace=False)
        array = []
        for line, row in enumerate(file_reader):
            # if line>1:
            file_reader_to_list = (';'.join(row)).split(';')
            array.append(file_reader_to_list)
        return array


def recording_file(array):
    with open(f'inputs.csv', 'w', encoding='utf-8') as file:
        for text in array:
            res_text = ";".join(text)
            file.writelines(f'{res_text}\n')



def read_index_row_data():
    with open('index_row_data.csv', 'r', encoding='utf-8') as csvfile:
        file_reader = csv.reader(csvfile, delimiter=';', skipinitialspace=False)
        for line in file_reader:
            index_row = line
        return index_row
def recording_index_row_data(index_row):
    with open(f'index_row_data.csv', 'w', encoding='utf-8') as file:
        file.writelines(f'{index_row}\n')