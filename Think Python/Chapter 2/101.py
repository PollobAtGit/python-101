# Variable (identifier) names must start with a letter
message = "I have something to tell you"
n = 17
pi = 3.141623

print(type(message))
print(type(pi))
print(type(n))

# Arithmetic computation

hour = 30
minute = 100
num = 5
exponent = 2

print(10 + 23)
print(hour - 1)
print(hour * 60 + minute)
print(hour * (60 + minute))

# Apparently, semi-colon is allowed at the end of the statement
print(hour * (60 + minute))

# Both of the followings are same
print(num ** exponent)
print(pow(num, exponent))

# '/' performs as a natural division operator
print(59 / hour)  # 1.9666...

# // performs floor division
print(59 // hour)  # 1

print(59 % hour)  # 29

print(type(59 / hour))  # <class 'float'>
print(type(59 // hour))  # <class 'int'>

print(hour * exponent)

aNum = 12

# Variables must be declared before usage
print(aNum + aNum)

