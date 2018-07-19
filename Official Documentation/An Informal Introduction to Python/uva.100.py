# not accepted in uva RTE

from sys import stdin

def three_n_plus_one(n, count):

    count = count + 1
    
    if n == 1:
        return count

    if n % 2 != 0:
        n = (3 * n) + 1
    else:
        n = n / 2

    return three_n_plus_one(n, count)

while True:
    try:
        line = input().split()

        i = int(line[0])
        j = int(line[1])
        
        m_t = max([(i, j, three_n_plus_one(x, 0)) for x in range(i, j + 1)])
        print(str(m_t[0]) + ' ' + str(m_t[1]) + ' ' + str(m_t[2]))
    except EOFError:
        break
