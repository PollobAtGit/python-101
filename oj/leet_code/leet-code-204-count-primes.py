# not working

class Solution:
    def count_primes_sieve(self, n):

        if n is not None:

            if n <= 2:
                return 0

            primes = [True] * n

            primes[0] = False
            primes[1] = False

            def falsify_non_primes(q):
                for i, _ in enumerate(primes[q + 1:], q + 1):
                    if i % q == 0 and primes[i]:
                        primes[i] = False

            falsify_non_primes(2)

            import math

            sqrt = int(math.sqrt(n)) + 1

            for x in range(3, sqrt, 2):
                if primes[x]:
                    falsify_non_primes(x)

            # print([i for i, y in enumerate(primes[:n]) if y])
            return len([i for i, y in enumerate(primes[:n]) if y])


    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n is not None:

            primes = []

            if n > 2:
                primes.append(2)

            if n > 3:
                primes.append(3)

            import math

            for x in range(5, n, 2):
                is_prime = True

                loop_max_range = int(math.sqrt(x)) + 1
                for y in range(3, loop_max_range, 2):
                    if x % y == 0:
                        is_prime = False

                if is_prime:
                    primes.append(x)

            return len(primes)

s = Solution()


print(s.count_primes_sieve(10))
print(s.count_primes_sieve(0))
print(s.count_primes_sieve(1))
print(s.count_primes_sieve(2))
print(s.count_primes_sieve(3))
print(s.count_primes_sieve(4))
print(s.count_primes_sieve(5))

print(s.count_primes_sieve(499979))
print(s.count_primes_sieve(1000))

