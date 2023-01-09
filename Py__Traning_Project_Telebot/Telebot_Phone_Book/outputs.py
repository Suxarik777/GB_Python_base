# ar = [['Фамилия', 'Имя', 'Телефон', 'Комментарий'], ['Иванов', 'Иван', '79854234245', 'Основной'], ['Петров', 'Пётр', '79854237463', 'Основной']]
from telebot import TeleBot, types
import csv



def show_all(arr):
    print('Вывод всего списка')
    for i in range(len(arr)):
        print(*arr[i])


def show_by_index(arr, index):
    print(f'Телефон под номером {index}:')
    print(*arr[0])
    print(*arr[index])


def show_by_filter(arr, stri):
    substring = str(stri)
    for i in range(1, len(arr)):
        for n in range(len(arr[i])):
            # print(arr[i][n])
            if arr[i][n].find(substring) > -1:
                print(*arr[i])


print_menu = 'Введите номер команды:\n1: Ввод\n2: Редактирование\n3: Экспорт\n4: Вывод\n7: Выйти'


def menu_search():
    print('Введите номер команды:',
    '\n 1: Вывод всего списка номеров',
    '\n 2: Вывод номера по индексу',
    '\n 3: Поиск номера по имени, фамилии, комментарию') 


def read_file():
    with open('input.csv', 'r', encoding='utf-8') as csvfile:
        file_reader = csv.reader(csvfile, delimiter=';', skipinitialspace=False)
        array = []
        for line, row in enumerate(file_reader):
            if line>1:
                file_reader_to_list = (';'.join(row)).split(';')
                array.append(file_reader_to_list[1:])
        return array

# print_menu()
# show_all(ar)
# print()
# n = int(input(f'Введите индекс нужного вам телефона:'))
# show_by_index(ar, n)
# print()
# m = input(f'Введите стоку в поиск: ')
# show_by_filter(ar, m)

