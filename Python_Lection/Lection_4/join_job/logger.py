from datetime import datetime as dt

def temperature_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('GB_Python_base/Python_Lection/Lection_4/join_job/log.csv', 'a') as file:
        file.write('{};temperature;{}\n'
                    .format(time, data))

def pressure_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('GB_Python_base/Python_Lection/Lection_4/join_job/log.csv', 'a') as file:
        file.write('{};prerssure;{}\n'
                    .format(time, data))

def wind_speed_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('GB_Python_base/Python_Lection/Lection_4/join_job/log.csv', 'a') as file:
        file.write('{};wind_speed;{}\n'
                    .format(time, data))