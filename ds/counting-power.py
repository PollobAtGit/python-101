# 2^4 = 2 * 2^3


def power_by_recursion(p, q):
    if p is not None and q is not None:
        if q == 0:
            return 1
        if q == 1:
            return p
        return p * power_by_recursion(p, q-1)


def test_code():
    print(power_by_recursion(2, 3))
    print(power_by_recursion(2, 4))
    print(power_by_recursion(2, 2))
    print(power_by_recursion(2, 1))
    print(power_by_recursion(2, 0))


test_code()
