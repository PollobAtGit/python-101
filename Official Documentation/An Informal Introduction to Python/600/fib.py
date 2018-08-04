def fib_rcrsv(n):
    if n == 1 or n == 2: return 1
    return fib(n - 1) + fib(n - 2)

def fib_iter(n):
    fibs = [1, 1]

    for i in range(2, n):
        fibs.append(fibs[i - 1] + fibs[i - 2])

    return fibs

def i_will_not_be_imported():
    return 10

# print(fib(7))
# print(fib_iter(7))
    
print('name of the module => ' + __name__)

if __name__ == '__main__':
    print('this is the starting method')

    import sys
    print(fib_iter(int(sys.argv[1])))
