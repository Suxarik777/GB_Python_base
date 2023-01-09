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