if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    print(sorted(set(arr))[::-1][1])
