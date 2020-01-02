def solution(A, K):
    if A and K is not None:
        for _ in range(K):
            last_element = A[len(A)-1]
            for i in range(len(A)-1, -1, -1):
                A[i] = A[i-1]
            A[0] = last_element
    return A


print(solution([3, 8, 9, 7, 6], 5))
print(solution([3, 8, 9, 7, 6], 4))
