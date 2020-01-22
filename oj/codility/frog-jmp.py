import math


def solution(X, Y, D):
    if X is not None and Y is not None and D is not None:
        distance_to_cover = Y - X
        if distance_to_cover > 0:
            return math.ceil(distance_to_cover / D)
        return -1
    return -1
