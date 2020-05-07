# ** allows method to receive a dictionary. python runtime does the trick of creating the dictionary
def definition_with_dic(**keywords):
    for key, value in keywords.items():
        print(f'{key} => {value}')


def concatenation(*arguments):
    return " | ".join([str(x) for x in arguments])


def concat_with_named_arguments(**kwargs):
    # kwargs is a dictionary
    return type(kwargs)


def concat(*arguments):
    # arguments is tuple not list
    return type(arguments)


# order of arguments matter in this case as we have argument, optional arguments, optional named argument
def lots_of_concatenation(arg, *args, **kwargs):
    result_str = arg

    for x in args:
        result_str += x

    for x in kwargs.values():
        result_str += x

    return result_str


if __name__ == "__main__":
    definition_with_dic(x='100', y='8',
                        z='None')  # note that the dictionary hasn't been created, it's created by python runtime
    # from the arguments

    print(concatenation(8, 9, 7))

    print(concat(7))

    print(concat_with_named_arguments(first_number=9))

    print(lots_of_concatenation('1', 'one', 'two', three='III', four='IV'))
