def add(a, b):
    return int(a) + int(b)

if __name__ == "__main__":
    print(add(*input().split(" ")))
