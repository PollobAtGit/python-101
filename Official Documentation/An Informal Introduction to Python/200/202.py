
# curly braces introduce sets 
basket= { 'apple', 'orange', 'apple', 'pear', 'orange'}
print(basket) # {'orange', 'apple', 'pear'}
print(len(basket))# 3

print('orange' in basket)# True
print('pear' in basket)# True
print('whatever' in basket)# False

a_set = set([1,2, 3, 1])
print(a_set)# {1, 2, 3}


# set comprehension
a_set = {x for x in [1, 2, 3, 1]}
print(a_set)# {1, 2, 3}

# dictionary

tel = { 'jack': 4098, 'sape': 4139}
print(tel)# {'jack': 4098, 'sape': 4139}
print(tel['jack'])# 4098

#This will throw exception
# print(tel['o'])

a_list = [1, 2, 3]
del a_list[2]
print(a_list)# 1, 2

# deleting dictionary element with key 'sape'
del tel['sape']
print(tel)# {'jack': 4098}

# from dictionary only the keys are being gathered to create the list & set
print(list(tel))# ['jack']
print(set(tel))# {'jack'}

# searching on key of the dictionary only
print('jack' in tel)# True

# Can't create dictionary from given information
# print(dict([1, 2, 3]))

# dcitionary constructor works properly for list of tuples only
print(dict([(1, 2), ('other', 3)]))# {1: 2, 'other': 3}

using_dictionary_comprehension = {x: x * 2for x in [1, 2, 3]}
print(using_dictionary_comprehension)# {1: 2, 2: 4, 3: 6}

# Note: comprehension is working on tuple not list
print([x for x in (1, 2, 3)])# [1, 2, 3]

print([x for x in {1, 2, 3}])

dic = {1: 'one', 2: 'two', 3: 'three'}
print([(x, dic[x]) for x in dic])# [(1, 'one'), (2, 'two'), (3, 'three')]

# using unpacking features
print([(y, z) for y, z in [(1, 2), (3, 4), (5, 6)]])# [(1, 2), (3, 4), (5, 6)] 

# confusing (little bit) if keys are string they can be put as first positional arguments
print(dict(a=2, b=3))# {'a': 2, 'b': 3}


knights = {'g' : 'pure', 'robbin' : 'brave'}

# items() provide the tuple for each item in dictionary
print([(a, b) for a, b in knights.items()])# [('g', 'pure'), ('robbin', 'brave')]

# [('item at => 0', 3), ('item at => 1', 2), ('item at => 2', 1)]
print([('item at => '  +str(i) , x) for i, x in enumerate([3, 2, 1])])

# [(0, 'g'), (1, 'robbin')]
print([(i, x) for i, x in enumerate(knights)])

# [(0, ('g', 'pure')), (1, ('robbin', 'brave'))]
print([(i, x) for i, x in enumerate(knights.items())])

# short cut for multiple loop
print([(a, b) for a, b in zip([1, 2], [3,4])])# [(1, 3), (2, 4)]

print(list(reversed([1, 2, 3])))# [3, 2, 1]
print(sorted([3, 2, 1]))# [1, 2, 3]

print(1 and 0)
print(1 or 0)
