def div_mod(x, y):
    if x is not None and y is not None:
        reminder = x % y
        quotient = int(x / y)

        # comma seperated values create a tuple. following is a tuple. braces are not required
        # interestingly we can return multiple values in this approach assuming they are part of a tuple
        return reminder, quotient

print((div_mod(20, 8))) # 4, 2
print(type(div_mod(20, 8)))

# declaring a tuple
t = 20, 8

# invalid syntax. why?
# a_t = (a = 30, b = 9)
# print(type(a_t))

# unpacking the tuple (t)
print(div_mod(*t))


import os

# we don't care about the first part of the array
_, file_name = os.path.split('/home/demo/other_demo/more_demo/202.py')
print(file_name)

# other essentially will be a list containing everything after 3rd element
first, second, three, *other = range(7)

# 0 1 2 [3 4 5 6]
print(first, second, three, other)

person_attributes = ('x', 'y@gmail.com', 10, 'nid card')

# ___rest___ values containing variable will always be an array. Here the source is a tuple still the last variable is a list
name, email, *other_attributes = person_attributes

print(name, email, other_attributes)

# exception will occur because ___unpacking___ ensures number of unpacked elements is the same as the number of elements expected
# name, email = ('a', (45.56, 8), 'other_text', 89)

# using __rest__ on first attributes, we want the last one only
*other_attributes, nid = person_attributes
print(other_attributes, nid)# ['x', 'y@gmail.com', 10] nid card

metro_areas = [
    ('Tokyo', 'JP', 36.33, (35.68772, 139.98)),
    ('Delhi NCR', 'India', -36.33, (-35.68772, -139.98)),
    ('Mexico City', 'Mexico', -36.33, (35.68772, -139.98))
]

fmt = "{:15} | {:9.4f} | {:9.4f}"

for city, country, whatever, (lat, longi) in metro_areas:
    if whatever < 0:
        print(fmt.format(city, lat, longi))

from collections import namedtuple


LatLong = namedtuple("lat_long", ['lat', 'lon'])

# no need to use array. instead we can give a space seperated string where each space seperated string will a property
# ... city_description ... will be used when the tuple will be printed not ... CityDescription ...
CityDescription = namedtuple("city_description", "city country i_dont_know_what lat_long")

for cd in metro_areas:

    # unpacking
    city_description = CityDescription(*cd)
    if(city_description.i_dont_know_what > 0):
        print(city_description)# city_description(city='Tokyo', country='JP', i_dont_know_what=36.33, lat_long=(35.68772, 139.98))

        # unpacking nested tuple to a stongly typed tuple
        print(LatLong(*city_description.lat_long))

print()
print('--------------------- metadata -------------------')
print()

print(CityDescription._fields)# ('city', 'country', 'i_dont_know_what', 'lat_long')
print(CityDescription._make(('Mexico City', 'Mexico', -36.33, (35.68772, -139.98))))
print(CityDescription._make(('Mexico City', 'Mexico', -36.33, (35.68772, -139.98)))._asdict())
