# not working

def test_cases():
    t = int(input())
    inputs = []
    for x in range(t):
        nums = input().split()
        inputs.append((int(nums[0]), int(nums[1])))
    return inputs


def generate_all_primes_until_one_billion():

    import math

    primes = [2, 3]

    # for x in range(5, 1000000000 + 1, 2):
    for x in range(5, 32000 + 1, 2):

        is_prime = True

        for y in range(3, int(math.sqrt(x)) + 1):
            if x % y == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(x)

    return primes

def primes(m, n):

    if m is not None and n is not None:

        import math

        all_primes = generate_all_primes_until_one_billion()

        print(all_primes)

        primes = []

        for x in all_primes:
            if x >= m and x <= n:
                primes.append(x)
            else:
                break       

        return primes


def main():

    inputs = test_cases();

    for x in inputs:
        for y in primes(x[0], x[1]):
            print(y)
        print()

main()