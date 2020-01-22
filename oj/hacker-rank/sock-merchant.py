def sockMerchant(n, ar):
    if ar:
        c = collections.Counter(ar)
        total_pair = 0
        for x, count in c.items():
            d = math.floor(count / 2)
            if d > 0:
                total_pair = total_pair + d
        return total_pair
