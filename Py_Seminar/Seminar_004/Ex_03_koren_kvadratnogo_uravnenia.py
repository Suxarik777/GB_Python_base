# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
#     С помощью математических формул нахождения корней квадратного уравнения

# x =-b+- корень(D) /2a



def solve(a, b, c):
    roots = []
    A1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    A2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    if A1 != A2:
        roots.append(A1)
        roots.append(A2)
    else:
        roots.append(A1)
    return roots

# второй вариант
# x1 + x2 = -b/a
# x1 + x2 = c/a


    
equation_list = []

for i in input("Введите числа через пробел: ").split():
    equation_list.append(int(i))


print(solve(*equation_list))


