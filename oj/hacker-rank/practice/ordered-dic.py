from collections import OrderedDict

if __name__ == "__main__":
    n = int(input())

    od = OrderedDict()

    for _ in range(n):
        parts = input().split()
        price = int(parts[len(parts) - 1])
        fruit = " ".join(parts[:len(parts)-1])

        if fruit in od:
            od[fruit] += price
        else:
            od[fruit] = price

    for x, price in od.items():
        print(x, price)
