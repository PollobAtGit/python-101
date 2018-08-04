def fib(n):
    if n == 1 or n == 2: return 1
    return fib(n - 1) + fib(n - 2)

def fib_iter(n):
    fibs = [1, 1]

    for i in range(2, n):
        fibs.append(fibs[i - 1] + fibs[i - 2])

    return fibs

# print(fib(7))
# print(fib_iter(7))
    
