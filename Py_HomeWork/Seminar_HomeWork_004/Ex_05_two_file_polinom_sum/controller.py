# 5 Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
# Коэффициенты могут быть как положительными, так и отрицательными.
# Степени многочленов могут отличаться.


import os

os.chdir(os.path.dirname(__file__))

def system_start():
    polynom_file_1 = 'polynom_1.txt'
    polynom_file_2 = 'polynom_2.txt'
    result_file = 'polynom_sum_two_result.txt'


    import func_read_file_in_string as read
    polynom1 = read.read_file(polynom_file_1)
    polynom2 = read.read_file(polynom_file_2)

    import func_transform_polinom as transform
    p1 = transform.transform_polynom(polynom1, polynom_file_1)
    p2 = transform.transform_polynom(polynom2, polynom_file_2)
    print(type(p1))

    import func_fill_coeff_missing as fill_cm
    tp1 = fill_cm.fill_missing_coeff(p1)
    tp2 = fill_cm.fill_missing_coeff(p2)

    import func_sum_polynom as f_sum
    result = f_sum.sum_polinom(tp1, tp2)

    import func_recording_file_in_md_or_txt as recording
    recording.call_record_func(len(result)-1, result, result_file)