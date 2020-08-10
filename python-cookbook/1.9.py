# 1.9 => FINDING COMMONALITIES BETWEEN DICTIONARIES

# discussion: dictionary has members .keys() & .items() which are guranteed to be unique for a
# dictionary. so set operations are available out of the box for these dictionary members

a = { 'HP': 500, 'DELL': 100, 'LENOVO': 130 } 

# b = { 'DELL': 45, 'APPLE': 456 }
b = { 'DELL': 100, 'APPLE': 456 }

print(a.keys() & b.keys())

# following considers (key, value) tuple
print(a.items() & b.items())
print(a.keys() ^ b.keys())
print(a.keys() | b.keys())
print(a.keys() - b.keys())

# problem: create dictionary from 'a' excluding LENOVO

# why doesn't following work but 'a.items()' work?
# print(dict(filter(lambda x: x[0] != 'LENOVO', a)))

print(dict(filter(lambda x: x[0] != 'LENOVO', a.items())))

print({x: a[x] for x in a.keys() - { 'HP', 'LENOVO' }})


