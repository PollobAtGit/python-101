
def division(p, q):
    if p is not None and q is not None:
        return p // q, p / q

if __name__ == "__main__":
    p, q = int(input()), int(input())
    
    d_i, d_f = division(p, q)
    print(d_i)
    print(d_f)

