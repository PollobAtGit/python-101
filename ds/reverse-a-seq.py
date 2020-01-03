def reverse(seq, start, end):
    if seq and start is not None and end is not None:
        if start < end:
            (seq[start], seq[end]) = (seq[end], seq[start])
            reverse(seq, start+1, end-1)


def reverse_by_slice(seq):
    if seq:
        if len(seq) == 1:
            return seq
        else:
            return reverse_by_slice(seq[1:])+[seq[0]]


def test_code(l):
    # reverse(l, 0, len(l)-1)
    print(reverse_by_slice(l))
    # print(l)


test_code([])
test_code([1])
test_code([1, 2])
test_code([1, 2, 3])
test_code([1, 2, 3, 4])
