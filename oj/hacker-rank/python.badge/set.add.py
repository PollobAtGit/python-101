def process_input():
    n = int(input())

    stamps = set()
    while n:
        stamps.add(input())
        n = n - 1 

    print(len(stamps))

process_input()
