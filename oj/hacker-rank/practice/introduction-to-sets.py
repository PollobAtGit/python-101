def average(array):
    if array:
        s = set(array)
        return sum(s) / len(s)
