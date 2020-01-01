def solution(l):
    if l:
        unpaired = 0
        for x in l:
            unpaired = unpaired ^ x

        return unpaired


print(solution([1, 1, 2]))
print(solution([9, 3, 9, 3, 9, 7, 9]))
