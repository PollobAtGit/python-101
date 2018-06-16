value = 10
valueTwo = 20

print(value + valueTwo)

needTrimming = " left trim : right trim "

print(needTrimming.lstrip())
print(needTrimming.rstrip())
print(needTrimming.strip())

exponent = 3 ** 9

print(exponent)# 19683

# Fun with string

print('python auto concat' ' magic')

# This is useful
print('python auto'
      ' auto concat'
      ' magic works better with'
      ' multi line')

initial_message = 'auto concat '

# Will not work because initial_messag is a variable. All of the strings
# need to be string literals
# print(initial_message 'doesn\'t'
#       'work with variables'
#       ' Both needs to be string literals')

print('auto concat ' 'doesn\'t'
      ' work with variables'
      ' Both needs to be string literals')
print()

# String repeatation (!) with * character
print('i am printed multiple times \n' * 5)

sample_string = 'Learning Python'

print('Full String: ' + sample_string)

print(sample_string[0] + sample_string[1])
print(sample_string[-2] + sample_string[-1])

print('Slicing ' + sample_string)

# begin -> end (2:4) => end is exclusive
print(sample_string[2:4])

# begin -> end rule is reversed when index in negative
print(sample_string[-4:-1])

print(sample_string[3:])# rning Python
print(sample_string[:4])# Lear

print(len(sample_string))# 15

# No index out of bound exception
print(sample_string[:100])# Learning Python
print(sample_string[-100:])# Learning Python

# Slicing + concat
print(sample_string[9:] + ' is scarey')

# How slices work
# +---+---+---+---+---+---+
#  | P | y | t | h | o | n |
# +---+---+---+---+---+---+
# 0   1   2   3   4   5   6
# -6  -5  -4  -3  -2  -1




