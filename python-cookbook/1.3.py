# 1.3 => FIXED SIZE DEQUE DROPS THE 1ST ELEMENT ADDED 

from collections import deque
from random import *

def deque_drops_first_element():
    dq = deque(maxlen=3)
    
    # following will be dropped when new item is inserted that exceeds length
    dq.append(1)
    dq.append(2)
    dq.append(3)
    dq.append(4)

    print(dq)

def yielding_random_numbers():
    for x in range(10):
        num = random()
        yield num

        # print statement will be executed after each 'yield' 
        print("prnt: " + str(num))

def random_numbers(n=5):
    for x in range(n):
        yield random()

def print_random_number():
    for random_number in random_numbers():
        print("Current random number: " + str(random_number))

deque_drops_first_element()
print(list(yielding_random_numbers()))
print_random_number()

