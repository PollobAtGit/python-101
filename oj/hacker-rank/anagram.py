def makeAnagram(a, b):
    if a is not None and b is not None:
        c_a = collections.Counter(a)
        c_b = collections.Counter(b)

        c_del_cnt = 0
        for item, count in c_a.items():
            if item in c_b:
                c_del_cnt = c_del_cnt + abs(count - c_b[item])
            else:
                c_del_cnt = c_del_cnt + count

        for item, count in c_b.items():
            if item not in c_a:
                c_del_cnt = c_del_cnt + count
        
        return c_del_cnt
