# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    if A:
        return sum(range(1, len(A)+2)) - sum(A)


print(solution([2, 3, 1, 5]))
