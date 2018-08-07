from decimal_to_other_base import decimal_to_other_base, decimal_to_hexa, decimal_to_twenty_six

def decimal_to_binary(num):
    if num:
        return decimal_to_other_base(num, 2)

def decimal_to_octal(num):
    if num:
        return decimal_to_other_base(num, 8)  

"""
print(decimal_to_binary(13))# [0, 1]
print(decimal_to_binary(10))# [0, 1]
print(decimal_to_binary(25))# [0, 1]
print(decimal_to_binary(38))# [0, 1]

print(decimal_to_octal(13))# [0, 1]
print(decimal_to_octal(10))# [0, 1]
print(decimal_to_octal(25))# [0, 1]
print(decimal_to_octal(38))# [0, 1]
"""

print(decimal_to_hexa(13))# [0, 1]
print(decimal_to_hexa(10))# [0, 1]
print(decimal_to_hexa(25))# [0, 1]
print(decimal_to_hexa(38))# [0, 1]
print(decimal_to_hexa(256))# [0, 1]

print(decimal_to_twenty_six(26))# [0, 1]
print(decimal_to_twenty_six(25))# [0, 1]
