def countingValleys(n, s):
    if s:
        level = 0
        valley_count = 0
        for x in s:
            delta = 1 if x == 'U' else -1
            if level == 0 and (level + delta) == -1:
                valley_count = valley_count + 1
            level = level + delta
        return valley_count
