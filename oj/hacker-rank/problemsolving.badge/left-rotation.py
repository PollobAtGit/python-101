#!/bin/python3

import math
import os
import random
import re
import sys

def left_rotate(n, d, a):
    indx = d % n
    return " ".join([str(x) for x in a[indx:] + a[:indx]])

if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    print(left_rotate(n, d, a))
