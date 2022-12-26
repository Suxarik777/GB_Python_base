# Функция для записи полинома в файл .md

def writing_file_md(k: int, user_list, user_file: str):
    with open(user_file, 'w', encoding='utf-8') as pol:
        if user_list[0] == 1:
            pol.write(f'$x^{k}')
        else:
            pol.write(f'${user_list[0]}x^{k}')

        for i in range(1,k+1):
            if user_list[i] != 0:
                if user_list[i] > 0:
                    pol.write('+')
                if user_list[i] != 1:
                    pol.write(f'{user_list[i]}')
                if i != k and i != k-1:
                    pol.write(f'x^{k-i}')
                elif i == k-1:
                    pol.write('x')
        pol.write('=0$')