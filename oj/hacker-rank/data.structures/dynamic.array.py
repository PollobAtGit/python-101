def dynamicArray(n, queries):
    
    arr = [[] for i in range(n)]
    lastAnswer = 0
    answers = []
    
    for i in range(0, len(queries)):
        q = queries[i][0]
        x = queries[i][1]
        y = queries[i][2]
        
        idx = (x ^ lastAnswer) % n
        
        if q == 1:
            arr[idx].append(y)
        if q == 2:
            lastAnswer = arr[idx][y % len(arr[idx])]
            answers.append(lastAnswer)
            
    return answers
