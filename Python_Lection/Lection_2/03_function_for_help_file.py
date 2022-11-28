import function_help_file # взяли другой файл пайтона (в нём у нас там функция)

print(function_help_file.function(1)) 
# в том скрипте вызвали функию отправили туда значение для работы функции) 


# если название файла большое, то можно указать альяс - сокращенное название

import function_help_file as name
print(name.function(1)) 