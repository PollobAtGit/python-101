
names_and_ages = [('alice', 89), ('karen', 7)]

print(names_and_ages)
print(dict(names_and_ages))
print(dict(a = '1', b = 5))

set_from_list = set(list(range(10)))

print(set_from_list)

try:
    None.split()
except :
    print("exception occurred")


try:
    print(dict(a = 'some', b = 'qrt')[8])
except KeyError as ke:
    print("key not found")
