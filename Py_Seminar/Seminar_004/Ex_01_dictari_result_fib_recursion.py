mem = {1: 0, 2: 1}
 
 
def fib(n):
    if n not in mem:
        mem[n] = fib(n - 1) + fib(n - 2)
 
    return mem[n]
 
 
print(fib(185))
print(mem)