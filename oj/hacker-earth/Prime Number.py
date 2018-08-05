def get_all_primes_till_n(n):
    if n:

        if n == 1:
            return []

        primes = ["2"]

        for x in range(3, n):
            if x % 2 == 0:
                continue

            is_prime = True
            for y in range(3, x, 2):
                if x % y == 0:
                    is_prime = False

            if is_prime:
                primes.append(str(x))

        return primes


if __name__ == "__main__":
    n = int(input())
    print(" ".join(get_all_primes_till_n(n)))
