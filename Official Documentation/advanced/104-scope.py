
x = 'global'

def local_scope():
    x = 'local'
    print(x)

local_scope()# local
print(x)

def local_change_global_x():
    
    # x will operate in global scope now
    global x

    # changing global x
    x = 'local - x'
    print(x)

local_change_global_x()
print(x)


def defining_global_variable():
    global q
    q = 100.23

# print(q)


# def other_outer():
    # x = None
def outer():
    
    # nolocal won't work here because 'nonlocal' searches for the given variable in it's outside lexical hierarchy
    # nonlocal x

    x = "from outer - outer"
    
    def inner():
        nonlocal x
        x = "from inner - inner"

        print(x)
    
    inner()# "from inner - inner"
    print(x)# "from inner - inner"

print()
print(x)
outer()


# global refers a variable in the module scope

def refer_to_outer_level_variable():
    print(x)

refer_to_outer_level_variable()# 'local - x'

