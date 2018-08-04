from eight_zero_one import CONSTANT


def read_file(file_name):
    return [line.replace("\n", "") for line in open(file_name)]


def safe_read_file(file_name):
    lines = []
    with open(file_name) as file:
        for line in file:
            lines.append(line.replace("\n", ""))

    return lines


file_name = "sample.txt"

print(read_file(file_name))
print(read_file(file_name))

print(safe_read_file(file_name))

print(CONSTANT)  # 99.99


def scope_test():
    def local_spam():
        spam = "from local_spam"

    def non_local_spam():
        nonlocal spam
        spam = "from non_local_spam"

    def global_spam():
        global spam
        spam = "from global_spam"

    spam = "just inside scope_test"

    local_spam()
    print(spam)  # just inside scope_test

    non_local_spam()
    print(spam)  # from non_local_spam

    global_spam()
    print(spam)  # from non_local_spam


scope_test()
print(spam)  # from global_spam


class SpamClass:
    def __init__(self):
        self.inside_spam = "initializing"

    def change_spam_message(self, msg):
        self.inside_spam = msg


sc = SpamClass()
print(sc.inside_spam)

sc.change_spam_message("other spams")

print(sc.inside_spam)


def outside_invocation():
    interesting_variable = 0

    def key_definition():
        # without nonlocal we can't return (!) the variable value
        nonlocal interesting_variable
        interesting_variable = 100

    inside_mechanism(key_definition)

    return interesting_variable


def inside_mechanism(key_func):
    key_func()


print(outside_invocation())

spam_cls = SpamClass()

# monkey patching
spam_cls.f = 1589
spam_cls.method_definition = lambda x: "ko => " + str(x)

print(spam_cls.f)
print(spam_cls.method_definition(10))


class Complex:
    def __init__(self, real_part, imaginary_part):
        self.r = real_part
        self.i = imaginary_part


complex_number = Complex(56, 78)

print(complex_number.r)
print(complex_number.i)

# literally delete the instance
del complex_number


def hidden_attribute_in_complex_type(n):
    complex_number = Complex(56, 89)

    complex_number.counter = 1

    while complex_number.counter < n:
        complex_number.counter = complex_number.counter + 1

    print(complex_number.counter)
    del complex_number.counter

    # will cause AttributeError bcause the attribute doesn't exist anymore
    # print(complex_number.counter)


hidden_attribute_in_complex_type(10)
