# MULTIPLE VALUES FOR SINGLE KEY

from collections import defaultdict

def get_random_default_dictionary():

    # not sending any list rather passing type name (list)
    d = defaultdict(list)

    d['computers'].append('HP')
    d['computers'].append('DELL')
    d['editors'].append('vim')
    d['editors'].append('visual studio code')
    
    return d

def get_random_default_dictionary_as_set():

    # passing type name 'set'
    d = defaultdict(set)

    d['computers'].add('HP')
    d['computers'].add('DELL')
    d['editors'].add('vim')
    d['editors'].add('visual studio code')
    
    return d

def default_dic_adds_and_element_if_not_found_when_searching():

    d = defaultdict(list)

    # following adds an element of list to the dictionary with key 'computers'
    v = d["computers"]

    print(d)

print(get_random_default_dictionary())
print(get_random_default_dictionary_as_set())
print(default_dic_adds_and_element_if_not_found_when_searching())
