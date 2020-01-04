# Read two integers from STDIN and print three lines where:
# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.

def arithmetic(p, q):
    if p is not None and q is not None:
        return p + q, p - q, p * q

if __name__ == "__main__":
    p = int(input())
    q = int(input())

    s, d, p = arithmetic(p, q)

    print(s)
    print(d)
    print(p)

