# Функция трансформации строки полинома для дальнейших матем. действий

def transform_polynom(user_polynom: str, user_file: str):
    polyn = user_polynom.replace('$', '')
    polyn = polyn.replace('**', '^')
    polyn = polyn.replace(' ', '')
    polyn = polyn[:-2]
    return polyn
