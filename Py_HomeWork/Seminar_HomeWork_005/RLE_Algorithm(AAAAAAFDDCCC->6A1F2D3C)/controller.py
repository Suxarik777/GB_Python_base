from menu import menu_user
from import_export_file import import_string, export_string
from modul_RLE import compressed_text, decompressed_text


def system_start():
    file_text = 'string_text.txt'
    code_file_text = 'code_text.txt'

    task_program = menu_user()

    if task_program == 'coding':
        string = import_string(file_text)
        print(f'Кодируем вот это: \n{string}')

        string_res = compressed_text(string)
        print(f'Получаем вот это: \n{string_res}')

        export_string(code_file_text, string_res)

    elif task_program == 'decoding':
        string = import_string(code_file_text)
        print(f'декодируем вот это: \n{string}')

        string_res = decompressed_text(string)
        print(f'Получаем вот это: \n{string_res}')

        export_string(file_text, string_res)

    print(f'''Результат работы программы смотри в репозитории:
    обычный текст - {file_text}
    закодированный текст - {code_file_text}''')

