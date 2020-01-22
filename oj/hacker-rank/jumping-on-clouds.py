def jumpingOnClouds(c):
    if c:
        jump_count = 0
        i = 0
        length = len(c)
        while i < length:
            if i + 2 < length and c[i+2] == 0:
                i = i+2
            else:
                i = i+1
            
            if not i >= length: # 7 - 1 = 6
                jump_count = jump_count + 1
        return jump_count
