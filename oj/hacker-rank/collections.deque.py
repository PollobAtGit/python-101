from collections import deque

if __name__ == "__main__":
    n = int(input())

    dq = deque()

    for _ in range(n):
        parts = input().split()
        op, v = parts[0], int(parts[1]) if len(parts) == 2 else None

        if op == "append" and v is not None:
            dq.append(v)
        elif op == "pop":
            dq.pop()
        elif op == "popleft":
            dq.popleft()
        elif op == "appendleft" and v is not None:
            dq.appendleft(v)

    for x in dq:
        print(x, end=' ')
