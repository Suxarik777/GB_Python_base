from user_interface import temeperature_view
from user_interface import wind_speed_view
from user_interface import pressure_view

def create(device = 1):
    style = 'style="font-size:30px;"' # описание стиля текса
    html = '<html>\n <head></head>\n <bodv>\n' # заготовка для html представления
    # далее идёт строка которая вписываем значения (форматируется)
    html += '   <p {}>Temperature: {} c</p>\n'\
        .format(style, temeperature_view(device))
    html += '   <p {}>Wind_speed: {} m/s</p>\n'\
        .format(style, wind_speed_view(device))
    html += '   <p {}>Pressure: {} mmHg</p>\n'\
        .format(style, pressure_view(device))

    with open('GB_Python_base/Python_Lection/Lection_4/join_job/index.html', 'w') as page: # создание файла
        page.write(html) # запись в файл
    
    return html

def new_create(data, device = 1): # добавили принятия данных с кортежа data_provider
    t, p, w = data # кладём этот кортеж сразу в переменные
    style = 'style="font-size:30px;"' # описание стиля текса
    html = '<html>\n <head></head>\n <bodv>\n' # заготовка для html представления
    html += '   <p {}>Temperature: {} c</p>\n'\
        .format(style, t) # вместо вызова метода из data_provider подставляем значения которые получили с кортежа
    html += '   <p {}>Wind_speed: {} m/s</p>\n'\
        .format(style, w)
    html += '   <p {}>Pressure: {} mmHg</p>\n'\
        .format(style, p)

    with open('GB_Python_base/Python_Lection/Lection_4/join_job/new_index.html', 'w') as page: # создание файла
        page.write(html) # запись в файл
    
    return data