#сумма двух чисел

a=1
b=2
c=a+b
print(c)


#= знак говорит о том что мы создаём путь до единички

a=[1,2,3]
b=a[:] #записываем ссылку на этот новый список
c=a+b
print(c)

print(10,11,12, sep="+", end='\n') #видим только тогда когда переносим на новую строку
print(10,11,12, sep="+")

print(10,11,12, sep="+", end='не переносить')
print(10,11,12, sep="+")

print(10,11,12, sep="+", end='')
print(10,11,12, sep="+")

print(10,11,12, sep="+") #номинально без end переносит
print(10,11,12, sep="+")