# Enter your code here. Read input from STDIN. Print output to STDOUT

# 2 4 5 9
# 2 4 11 12

def get_symmetric_diff(p, q):
    if p and q:
        a = set(p)
        b = set(q)

        a_inter_b = a.intersection(b)
        b_inter_a = b.intersection(a)

        for x in a_inter_b:
            a.discard(x)

        for x in b_inter_a:
            b.discard(x)

        return sorted(a.union(b))

def take_input():
    input()
    m_arr = list(map(int, input().split()))
    input()
    n_arr = list(map(int, input().split()))

    for x in get_symmetric_diff(m_arr, n_arr):
        print(x)

take_input()

