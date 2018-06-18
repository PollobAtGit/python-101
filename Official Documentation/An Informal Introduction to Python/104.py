def return_n_fib_numbers(n):
    fibs = []

    a, b = 0, 1

    while  a < n:
        fibs.append(a)
        a, b = b, a + b

    return fibs

print(return_n_fib_numbers(10))
print(return_n_fib_numbers(20))
    
def ask_ok(prompt = 'Enter Yes/No\n', retries = 4, reminder = 'Please try again'):
    while True:
        ok = input(prompt)

        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nope'):
            return False

        retries = retries - 1

        if retries < 0:
            raise ValueError('Invalid User Response')

        print(reminder)

print(ask_ok())

# in is a seperate operator from if .. else
print('yes' in ('yes', 'y'))

# default argument without literals

i = 10

def print_value_of_i_from_before(n = i):
    print(n)

i = 20

# prints 10 not 20. Which means n is bound with the value with i when function
# dfinition was being constructed
print_value_of_i_from_before()

# default values are evaluated only once during method composition time not when it's being invoked

def default_list_argument(x, l = []):
    l.append(x)
    return l

print(default_list_argument(10))# [10]

# Original list has the reference it's not destroyed
print(default_list_argument(20))# [10, 20]

# given number will be appended to the original list
print(default_list_argument(30))# [10, 20, 30]


default_list = [-9]

def return_list(l = default_list):
    return l

# This assignment will not impact 'l' in return_list function
default_list = [56]

print(return_list())# [-9]
print(default_list)

# Not sharing the list with sub-sequent invocation of the method

def none_as_default(x, l = None):
    if l is None:
        l = []
    l.append(x)
    return l

print(none_as_default(-6))# -6
print(none_as_default(9.6))# 9.6
    
