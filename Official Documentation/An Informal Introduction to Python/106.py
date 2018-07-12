def list_operations(lst):
    lst.append(23) # append mutates the list
    return lst

def list_extend(lst):
    lst.extend(['A', 'B']) # extend also mutates the list
    return lst

def insert_at_list(lst, i, v):
    # if index given in insert(..) doesn't exist then the value (v) will be put the
    # latest blank place
    # insert doesn't replace the value at that index
    lst.insert(i, v)
    return lst

def remove_from_lst(lst, v):
    lst.remove(v)
    return lst

global_list = [5, 10, 15, 20]

def pop_from_global_list():
    return global_list.pop()

def pop_from_list(lst):
    return lst.pop()

print(list_operations([]))
print(list_extend([15, 89]))
print(insert_at_list([89, 98, 109], 1, 'polli')) # [89, 'polli', 98, 109]
print(insert_at_list(insert_at_list([89, 98, 109], 1, 'polli'), 2, -989.23)) # [89, 'polli', -989.23, 98, 109]
print(remove_from_lst([89, 98, 109], 109)) # [89, 98]
print(remove_from_lst(remove_from_lst([89, 98, 109], 109), 89)) # [98]
print(pop_from_global_list()) # 20

print(global_list) # [5, 10, 15]

a_list = ['other', None, 458] # .pop() pops from the end of the list
print(pop_from_list(a_list)) # 458
print(a_list) # ['other', None]

print(insert_at_list(insert_at_list([], 1, 20), 20, 89)) # [20, 89]
