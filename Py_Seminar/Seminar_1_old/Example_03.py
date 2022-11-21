#2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
    
#   Примеры:
    
#    - 1, 4, 8, 7, 5 -> 8
#    - 78, 55, 36, 90, 2 -> 90



a = int(input('Введите 1 число: '))
b = int(input('Введите 1 число: '))
c = int(input('Введите 1 число: '))
d = int(input('Введите 1 число: '))
e = int(input('Введите 1 число: '))

max11 = a # не использовать max это резерв python
if b > max11:
    max11 = b
if c > max11:
    max11 = c
if d > max11:
    max11 = d
if e > max11:
    max11 = e
print(a,b,c,d,e)
print(max11)

#разница if if if if = это каждый раз проверит линейно заподряд
#а если мы фигачим if elif = то он найдя 
#следующее максимальное, он прекратит цикл проверок



fiver = list(map(int, input('Введите 5 чисел через пробел: ').split()))
max=fiver[0]
for i in range(len(fiver)):
    if fiver[i]>max:
        max=fiver[i]
print(max)


#цикл for

a = int (input("введите a: "))
b = int (input("введите b: "))
c = int (input("введите c: "))
d = int (input("введите d: "))
e = int (input("введите e: "))

m = a
for i in b,c,d,e:
     if i>m: m=i
print(m)


#самое быстрое
print(max(1, 4, 998, 7, 5))