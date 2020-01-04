
def loop(n):
    if n is not None:
        return [x * x for x in range(n)]

if __name__ == "__main__":
    n = int(input())

    for x in loop(n):
        print(x)
