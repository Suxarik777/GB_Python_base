from user_interface import temeperature_view
from user_interface import wind_speed_view
from user_interface import pressure_view


def new_create(data, device = 1):
    t, p, w = data
    t = t * 1.8 + 32 # таким побразом через формулу меняем значения C(цельсия) на 
    xml = '<xml>\n'
    xml += '    <temperature units = "f">{}</temperature>\n'\
        .format(t)
    xml += '    <wind_speed units = "m/s">{}</temperature>\n'\
        .format(w)
    xml += '    <pressure units = "mmHg">{}</temperature>\n'\
        .format(p)
    xml += '</xml>'

    with open('GB_Python_base/Python_Lection/Lection_4/join_job/new_data.xml', 'w') as page: # создание файла
        page.write(xml) # запись в файл
    
    return data



def create(device = 1):
    xml = '<xml>\n'
    xml += '    <temperature units = "c">{}</temperature>\n'\
        .format(temeperature_view(device))
    xml += '    <wind_speed units = "c">{}</temperature>\n'\
        .format(wind_speed_view(device))
    xml += '    <pressure units = "c">{}</temperature>\n'\
        .format(pressure_view(device))
    xml += '</xml>'

    with open('GB_Python_base/Python_Lection/Lection_4/join_job/data.xml', 'w') as page: # создание файла
        page.write(xml) # запись в файл
    
    return xml
    
    