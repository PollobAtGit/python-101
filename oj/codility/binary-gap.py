def solution(N):
    if N is not None:
        binary_rep = "{:b}".format(N).strip('0')

        length = 0
        highest_length = 0

        for i in range(len(binary_rep)):
            if binary_rep[i] == '0':
                length = length + 1
            if binary_rep[i] == '1':
                highest_length = max(highest_length, length)
                length = 0
        return highest_length
    return -1


print(solution(32))
print(solution(9))
print(solution(1041))
