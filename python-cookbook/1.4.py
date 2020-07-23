## GET N LARGEST OR SMALLEST ELEMENTS

## DISCUSSION: IF ARRAY ELEMENT COUNT IS THE SAME AS N THEN IT'S FASTER TO USE
## SORTED(...)  

import heapq

def n_smallest(items, filter_criteria=None):
    if filter_criteria:
        return heapq.nsmallest(3, items, filter_criteria)
    return heapq.nsmallest(3, items)

def n_largest(items):
    return heapq.nlargest(3, items)

def heapify(items):
    return (heapq.heapify(items))

def test_code_with_custom_record():

    computers = [
            {'name':"DELL",    'price': 34.67 },
            {'name':"HP",      'price': 35.67 },       
            {'name':"APPLE",   'price': 36.67 },       
            {'name':"LENOVO",  'price': 4.67 }        
    ]

    # print(computers)
    # print(type(computers[0]))
    
    print(n_smallest(computers, lambda x : x['price']))

def test_code():

    items = [9, 4, 5, -4, 55, 100]

    print(n_smallest(items))
    print(n_largest(items))

    # slice creates a copy of the original list
    heap = items[:]

    heapify(heap)
    print(heap)
    print(items)

    print(heapq.heappop(heap))
    print(heapq.heappop(heap))
    print(heap)

test_code()
test_code_with_custom_record()

