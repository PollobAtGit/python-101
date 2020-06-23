n = int(input())
s = set(map(int, input().split()))

op_count = int(input())

# pop, remove and/or discard

for _ in range(op_count):
    i_splitted = input().split()
    op, v = i_splitted[0], i_splitted[1] if len(i_splitted) == 2 else ""
    if op == 'pop':
        s.pop()
    if op == 'remove':
        s.remove(int(v))
    if op == 'discard':
        s.discard(int(v))

print(sum(s))

