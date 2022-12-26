# Функция для выбора функции для записи файла в зависимости от типа файла: .md или .txt

def call_record_func(k: int, coeff_polinom: list, user_file: str):
    if user_file[-3:len(user_file)] == '.md':

        import func_write_polinom_md as file
        file.writing_file_md(k, coeff_polinom, user_file)

    elif user_file[-4:len(user_file)] == '.txt':

        import func_write_polinom_txt as file
        file.writing_file_txt(k, coeff_polinom, user_file)

    else:
        print('Не определён тип файла. Распознаются типы: .md и txt')