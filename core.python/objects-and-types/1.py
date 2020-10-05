m = [1, 2, 4]


def modify(q):
    # append will mutate the original passed list
    q.append(12)
    return q


def modify_with_internal_copy(q):
    # a new list is being created meaning any modification to this
    # list will not have impact on the original list

    q = list(q)
    q.append(99)
    return q


def reassign(q):
    # here both the original list pointer/variable and q refers to the same object in memory
    # but after reassigning to q now q refers to the new object in memory while the original
    # pointer refers to the old object in memory
    q = []
    return q


def return_what_received(q):
    return q


# q will be evaluated only once meaning at each invocation of this method the
def default_argument_values_are_evaluated_once(q={}):
    if 1 in q:
        q[2] = "two"
    else:
        q[1] = "one"
    return q


if __name__ == "__main__":
    print(modify(m))
    print(m)

    print(modify_with_internal_copy(m))
    print(m)

    print(reassign(m))
    print(m)

    print(m is return_what_received(m))
    print(id(m), id(return_what_received(m)))

    print(default_argument_values_are_evaluated_once())
    print(default_argument_values_are_evaluated_once())
