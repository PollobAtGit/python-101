def default_argument_behavior(arg):
    print(arg)


# [positional arguments] / .... [ default argument behavior ]
def positional_argument_behavior(arg, /):
    print(arg)


# ... [default argument behavior] ... * [keyword arguments]
def keyword_arguments_only(*, arg_one, arg_two):
    print(arg_one, arg_two)


# [positional arguments] / .... [ default behavior ] .... * [keyword arguments]
def combining_positional_and_keyword_arguments(arg_one, arg_two, /, arg, *, arg_three, arg_four):
    print(arg, arg_one, arg_two, arg_three, arg_four)


# multiple usage of '*' is not allowed which prevents using both [keyword arguments with unpacking operator (
# **kwargs) along with keyword argument special character]

# '/' must be used BEFORE any usage of '*' which prevents usage of unpacking arguments as positional argument in
# argument list

# all of the below are invalid

# def q(*args, /): pass
# def q(**args, /): pass
# def q(*, *args): pass
# def q(*, **args): pass


# 'y' must be invoked as keyword only argument
# defining argument is valid after variadic argument definition but in runtime the argument needs to be invoked as
# keyword argument
def q(*args, y):
    return " | ".join(args + tuple(y))


# during unpacking exact number of arguments needs to be in the sequence that will be unpacked. so both of the following
# will throw runtime exception

# add(*[])
# add(*[1, 2, 3, 4])

def add(x, y, z):
    return x + y + z


if __name__ == "__main__":
    default_argument_behavior(10)
    default_argument_behavior(arg=10)

    # following is invalid because of 'named argument'
    # positional_argument_behavior(arg=10)

    positional_argument_behavior(89)

    keyword_arguments_only(arg_two=9, arg_one=10)

    # following is invalid because method only takes keyword arguments
    # keyword_arguments_only(88, 99)

    combining_positional_and_keyword_arguments(10, 9, 10, arg_three='q', arg_four='r')
    combining_positional_and_keyword_arguments(10, 9, arg=10, arg_three='q', arg_four='r')

    # y is being invoked as keyword only argument
    print(q('8', '9', '10', y='88'))

    # unpack lists
    print(add(*[1, 2, 3]))

    # unpacking dictionary. ** unpacks the values. * unpacks the keys
    print(add(*{'one': 1, 'two': 2, 'three': 3}))  # onethwothree

    try:
        # during unpacking dictionary values, keys must match with method argument list (based on name)
        print(add(**{'one': 1, 'two': 2, 'three': 3}))
    except TypeError as e:
        print(e.args)

    # dictionary unpacking with values. keys needs to match
    print(add(**{'x': 1, 'y': 2, 'z': 3}))
