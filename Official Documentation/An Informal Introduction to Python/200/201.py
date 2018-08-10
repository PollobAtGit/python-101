import math

def einn(func, x):
    if x >= 0:
        return str(func(x))
    else:
        return "Can't do operation of negative"

print(math)

inpt_str = input()
inpt = int(inpt_str)

print(math.sin(inpt))
print(math.sin(-1 * inpt))

print(einn(math.log10, inpt))
print(einn(math.sqrt, inpt))

# k is global in this scope
for k in range(10):
    # python is not block scoped
    t = -99

print(k)# 9
print(t)# -99
