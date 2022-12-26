# Функция суммирования двух многочленов

def addition_coefficients(user_polinom: list, complimentary: int) -> list:
    for i in range(complimentary):
        user_polinom.insert(0, 0)
    return user_polinom


def sum_polinom(tp1: list, tp2: list) -> list:
    if len(tp1) != len(tp2):
        complementary = abs(len(tp1) - len(tp2))
        if len(tp1) < len(tp2):
            tp1 = addition_coefficients(tp1, complementary)
        else:
            tp2 = addition_coefficients(tp2, complementary)
    result = []
    for i in range(len(tp1)):
        help_tp_1 = int(tp1[i])
        help_tp_2 = int(tp2[i])
        result.append(help_tp_1 + help_tp_2)
    return result