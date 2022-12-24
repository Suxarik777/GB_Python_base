# соединяем два модуля и делаем кнопку

import model_sum as model
import view

def button_click():
    value_a = view.get_value() #+ делаем метод который будет принимать значения 
    value_b = view.get_value()
    model.init(value_a, value_b)#проводим инициализацию двух значений, отправляем посчитать 
    result = model.do_it()
    view.view_data(result, 'result = ')

