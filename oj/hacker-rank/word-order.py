from collections import OrderedDict

if __name__ == "__main__":
    n = int(input())
    od = OrderedDict()
    for _ in range(n):
        word = input()
        if word in od:
            od[word] = od[word] + 1
        else:
            od[word] = 1

    print(len(od))
    for _, v in od.items():
        print(v, end=' ')
