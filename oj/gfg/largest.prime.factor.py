def find_primes(n):

    primes = [True for i in range(n + 1)]

    for v in range(2, n):
        i = 2
        while v * i <= n:
            primes[v * i] = False
            i = i + 1

    return [i for i, v in enumerate(primes) if v and i > 1]

def largestPrimeFactor (n):

    primes = find_primes(n)

    return primes[len(primes) - 1]

def print_result(n):
    v = find_primes(n)
    print(v, len(v), largestPrimeFactor(n))

print_result(15)
print_result(25)
print_result(50)
print_result(100)
print_result(97)

