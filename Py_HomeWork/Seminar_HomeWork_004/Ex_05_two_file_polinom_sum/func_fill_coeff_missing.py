# Функция для заполнения недостающих коэффициентов многочлена

def num_list(p: str, a: str) -> int:
    if p.index(a) == 0:
        n = 1
    elif p.index(a) ==1:
        if p[0] == '-':
            n = -1
        elif p[0] == '+':
            n = 1
        else:
            n = p[0]
    else:
        n = int(p[:p.index(a)])
    return n

def degree_list(p: str) -> int:
    if p.find('-') != - 1and p.find('+') != -1:
        ind = min(p.index('-'), p.index('+'))
    elif p.find('-') != - 1and p.find('+') == -1:
        ind = p.index('-')
    elif p.find('-') == - 1and p.find('+') != -1:
        ind = p.index('+')
    else:
        ind = len(p)
    return ind

def fill_missing_coeff(p: str) -> list:
    n = []
    degree = []
    while len(p) > 0:
        if p.find('x^') != -1:
            n.append(num_list(p, 'x^'))
            p = p[:0] + p[p.index('x^'):]
            ind = degree_list(p)
            degree.append(int(p[2:ind]))
            p = p[:0] + p[ind:]
        elif p.find('x') != -1:
            n.append(num_list(p, 'x'))
            p = p[:0] + p[p.index('x'):]
            ind = degree_list(p)
            degree.append(1)
            p = p[:0] + p[1:]
        else:
            n.append(int(p[:len(p)]))
            degree.append(0)
            p = p[:0] + p[len(p):]
    for i in range(1, len(n)):
        if degree[i-1] - degree[i] != 1:
            for j in range((degree[i-1] - degree[i])-1):
                n.insert(i+j, 0)
                degree.insert(i+j, degree[i+j-1]-1)
    if degree[-1] != 0:
        for i in range(len(degree), len(degree) + degree[-1]):
                n.insert(i, 0)
                degree.insert(i, degree[i-1]-1)
    return n