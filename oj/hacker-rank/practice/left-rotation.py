
# 1 2 3 4 5 => [4] [2]

# 2 3 4 5 1
# 3 4 5 1 2

# 4
# 3

# 1.. 2 3 4 5 1
# 2.. 3 4 5 1 2
# 3.. 4 5 1 2 3
# 4.. 5 1 2 3 4

def rotate_left(s, n):
    if s is not None:
        for _ in range(n):
            f = s[0]
            for i in range(len(s) - 1):
                s[i] = s[i+1]
            s[len(s) - 1] = f 
        return s

def rotate_left_via_slice(s, n):
    if s is not None and n is not None:
        # len(s) > n
        return s[n:] + s[:n]

def rotate_left_in_o(s, n):
    if s is not None and n is not None:
        return rotate_left(s, n if len(s) > n else n % len(s))

def test_code():
    s = list((map(int, input().split())))
    n = int(input())

    print(rotate_left_via_slice(s, n))

test_code()

