basket = { 'basket', 'orange', 'pear', 'orange' , 'ata' }

print(type(basket))

# Duplication removed
print(basket) # {'pear', 'basket', 'orange'}
print('orange' in basket) # True
print('cannabis' in basket) # False

print(basket)

poped_data = basket.pop() # pop takes data from 1st index in case of set
print([1, 2].pop()) # pop takes last element from list in case of array/list

poped_data_char_set = set(poped_data )

print(poped_data)

# duplicates removed
print(poped_data_char_set) # {'a', 't'}

a = set('123')
b = set('234')

# set minus
print(a - b)# {'1'}

# union
print(a | b) # {'1', '3', '4', '2'}

# intersection
print(a & b) # {'2', '3'}

# letters in a or b but not in both
# sql: full join (a.id is null or b.id is null)
print(a ^ b)

# list comprehension
print({ x for x in a if x not in '39' })# {'1', '2'}


