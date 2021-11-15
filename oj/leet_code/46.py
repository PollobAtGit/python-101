
def p(v):
    print(v)

results = []

def perm(arr):

    if not arr:
        return

    if len(arr) == 1:
        return arr

    if len(arr) == 2:
        return [[arr[0], arr[1]], [arr[1], arr[0]]]

    current = arr[0]

    permutations = perm(arr[1:])

    for i in range(len(permutations)):
        permutations[i].append(current)
        results.append(permutations[i])

    perm(arr[:1] + arr[2:])


def permute(arr):
    if not arr:
        return []
    if len(arr) == 1:
        return arr
    if len(arr) == 2:
        return [[arr[0], arr[1]], [arr[1], arr[0]]]

    result = []
    current = arr[0]
    
    for i in range(len(arr)):

        v = permute(arr[:i] + arr[i+1:])

        for j in range(len(v)):
            result.append(v[j] + [arr[j]])


    return result

p(permute([]) == [])
p(permute([1]) == [1])
p(permute([1, 2]) == [[1, 2], [2, 1]])
p(permute([1, 2, 3]) == [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]])

p(permute([1, 2, 3])) 

