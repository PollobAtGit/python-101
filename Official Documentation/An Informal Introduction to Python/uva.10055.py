def diff(a, b):
    return abs(a - b)   

while True:
    try:
        line = input().split()
        print(diff(int(line[0]), int(line[1])))
    except EOFError:
        break

        
    
