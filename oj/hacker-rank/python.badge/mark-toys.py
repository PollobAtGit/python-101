# 7 50
# 1 12 5 111 200 1000 10
# 1 5 10 12 111 200 1000

def max_toys(s, t):
    if s is not None and t is not None:
        s_sorted = sorted(s)
        curnt_sum = 0
        for i, x in enumerate(s_sorted):
            if curnt_sum + x <= t:
                curnt_sum += x
            else:
                break
        return i

def test_code():
    prices = list(map(int, input().split()))
    k = int(input())

    print(max_toys(prices, k))

test_code()


