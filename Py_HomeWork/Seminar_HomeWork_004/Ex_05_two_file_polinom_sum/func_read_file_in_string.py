# Функция присваивания строке содержимого текстового файла

def read_file(name_file):
    with open(name_file, 'r', encoding='utf-8') as text:
        result = text.read()
        return result
