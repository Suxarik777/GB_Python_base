a = '1 + 2 + 3'

print(eval(a)) # 6

# сломается
a = '1 + b + 3'
print(eval(b)) #64 посчитает букву цифрой


# exec открывает доступ к память
c = 'd = 22'
exec(d)
print(d + 2)

# например
с = 'txt.txt'
exec(c) # цуликом открывает доступ полностью к файлу


# 'sudo rm -rf /*' # команда судного дня сносит целиком жесткий диск