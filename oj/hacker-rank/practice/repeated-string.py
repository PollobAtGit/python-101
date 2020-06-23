
# aba 10
# 7

# abcac 10
# 4

# 7 / 3 => 3 => abaabaabaa ba

import math
import collections

def find_repeated_concat(s, n):
    if s is not None and n is not None:
        while len(s) < n:
            s = s + s
        c = collections.Counter(s[:10])
        return c['a']

# len(s) * i_c 
# aba 10 => (10 - 3) / 3 => 7 / 3 => 3 => 
# 2
# 3 * 3 % 10

def find_repeated(s, n):
    if s is not None and n is not None:
        i_c = math.ceil(((n - len(s)) / len(s)))
        total_length = (len(s) * i_c) + 1
        partial_count = collections.Counter(s[total_length % n])['a']
        return (i_c * collections.Counter(s)['a']) + partial_count

# not solved ... wrong answer
if __name__ == "__main__":
    s = input()
    n = int(input())

    print(find_repeated(s, n))

