
# if .. elseif

# x = int(input('Enter an input number => \n'))
x = 18
print('You entered ' + str(x))

y = 100

if x < 0:
    y = y - 1
elif x < 10:
    y = y - 10
elif x < 50:
    y = y - 50
else:
    y = y - y

print(y)
    
# for ... each

words = ['cat', 'window', 'other']

for word in words:
    print('Length of [' + word + '] is ' + str(len(word)))


# slicing before iteration

for w in words[:]:
    # will not work properly without slicing because in that case an
    # infinite list will be created
    if(len(w) > 3):
        words.insert(0, '0:0X')

print(words)

# Generate sequence

# range by default starts from 0. Given number is exclusive
for num in range(9):
    print(num)

for num in range(15, 25):
    print(num)# prints until 24 starting from 15

# Starts from -50 increments by -3 ends before -80 is encountered
for num in range(-50, -80, -3):
    print(num)

# iterate over sequence with index (using range along with len on sequence)
for i in range(len(words)):
    print('Element at index: [' + str(i) + '] = {' + words[i] + '}')

# Element at index: [0] = {0:0X}
# Element at index: [1] = {0:0X}
# Element at index: [2] = {cat}
# Element at index: [3] = {window}
# Element at index: [4] = {other}

# Just an iterator object
# range(0, 5)
print(range(5))

print(list(range(10))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# Find primes until 10
for num in range(2, 10):
    for d in range(2, num):
        if num % d == 0:
            print(str(num) + ' is not a prime')
            break
    # else is tighted with for not with if...else. It will invoked if for ... is terminated with break (what about continue?)
    else:
        print(str(num) + ' is prime')

# continue
for num in range(1, 11):
    if num % 2 == 0:
        print(str(num) + ' is even')
        continue
    print(str(num) + ' is odd')

# Python function

def odd_or_even_till_n(n):
    for num in range(1, n + 1):
        if num % 2 == 0:
            print(str(num) + ' is even')
            continue
        print(str(num) + ' is odd')

print('\nOdd or even:\n')
odd_or_even_till_n(10)
        
print('\nOdd or even:\n')
odd_or_even_till_n(25)


