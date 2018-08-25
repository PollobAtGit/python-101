symbols = '$¢r£¥€¤ca'

symbol_asciis = [ord(ch) for ch in symbols]

print(symbol_asciis)  # [36, 162, 163, 165, 8364, 164]

unicode_characters = [{ch: ord(ch)}for ch in symbols if ord(ch) > 127]
non_unicode_characters = [{ch: ord(ch)} for ch in symbols if ord(ch) < 127]

print(unicode_characters)
print(non_unicode_characters)

# list comprehension is way better than filter
print([x for x in symbols if ord(x) < 127])

# filter returns iterator rather than a ...list... that's why we need to apply ...list... on it
print(list(filter(lambda x: ord(x) < 127, symbols)))

print(list(map(lambda x: ord(x), symbols)))

# much better compared to the above approach. given function ...ord... is applied on each character
print(list(map(ord, symbols)))

print(list(filter(lambda x: x < 127, map(ord, symbols))))
print([x for x in [ord(x) for x in symbols] if x < 127])

colors = ['black', 'white']
sizes = ['M', 'L', 'S']

print([(y, x) for x in colors for y in sizes])
print(sorted([(y, x) for x in colors for y in sizes]))
print(sorted([(y, x) for x in colors for y in sizes], key = lambda x: x[1], reverse = True))
print(sorted([(y, x) for x in colors for y in sizes], key = lambda x: x[1], reverse = False))

print()

# the portion inside ...tuple... is generator comprehension not list comprehension
# wrap the expression for list compression inside bracket instead of square bracket
# when possible it's ok to drop the bracket

symbols_gen= (ord(x) for x in symbols)
tuple_of_symbols = tuple(symbols_gen)

print(tuple_of_symbols)

# tuple defines __getitem__ so slicing works
print(tuple_of_symbols[5:])

# slicing on tuple
# slicing doesn't throw exception when index range is out of range for the tuple
print((1,)[50:])

import array

# what the fuck does ___array.array___ does?
print(array.array('I', (ord(x) for x in symbols)))

print(list(("%s %s" % (x, y) for x in colors for y in sizes)))

# note: not using list comprehension rather generator comprehension
for q in ("%s %s" % (x, y) for x in sizes for y in colors):
    print(q)

import collections

# Book(publisher='abc', publishing_date='1/1/2018')
# la la la ... curry function
print(collections.namedtuple('Book', ['publisher', 'publishing_date'])(publisher = 'abc', publishing_date = '1/1/2018'))

Book = collections.namedtuple('Book', ['publisher', 'publishing_date'])

# tuples and classes are not same in python
# tuple unpacking to properties
publisher, publishing_date = Book(publisher = 'xyz', publishing_date = 89)

# XYZ 89
print(publisher, publishing_date)
print('publishing date : ' + str(publishing_date))
print('publishing date : %d' % publishing_date)

traveler_ids = [('usa', '123'), ('bra', '456'), ('bd', '789')]
print(traveler_ids)

import time
nested_tuple = ('usa', (10, 100, (time.clock(),)))
country, other = nested_tuple
print(country, other)

tenth, hundreth, clocked = other
print(tenth, hundreth, clocked)

# how to unpack single tuple with single element
# clocked_time, a = clocked
# print(clocked_time)

# nested tuple unpacking
a, (b, c, (d, e)) = ('arg', (10.23, 89, (time.clock(), -99)))
print(a, b, c, d, e)
