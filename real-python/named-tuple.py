from collections import namedtuple

# c will be used to create type instances
# 'Car' is the type name

c = namedtuple('Car', 'color mileage')

car = c(color='black', mileage=500)

print(car)
print(type(car)) # prints 'Car' not 'c'

copy_of_car_with_color_mod = car._replace(color='white')

print(copy_of_car_with_color_mod)
print(c)

print(id(copy_of_car_with_color_mod))
print(id(c))

try:
    # following will throw exception because copy_of_car_with_color_mod is a tuple not class instance
    copy_of_car_with_color_mod.color = ''
except AttributeError as ae:
    print(ae)
