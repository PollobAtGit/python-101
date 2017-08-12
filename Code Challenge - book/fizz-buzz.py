def fizzbuzz(n):

result = []

for i in range(1, n + 1):
add = ''

if i % 3 == 0:
add += 'Fizz'

if i % 5 == 0:
add += 'Buzz'

if add == '':
result.append(i)
else:
result.append(add)
return result
