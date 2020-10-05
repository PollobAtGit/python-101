import math

city_list = ('dhaka', 'washington dc', 'london')

print(city_list)

# x will be available outside scope of the for loop because loop doesn't introduce any scope
for x in range(10, 15):
    # add element to tuple
    # this is the only way to increase tuple size
    city_list += (str(x),)

print(city_list)
print(len(city_list))


def get_numbers(cities):
    for c in cities:
        try:
            int(c)
        except:
            yield c


print(list(get_numbers(city_list)))

print()


def check_if_cities_exist():
    for city in get_numbers(city_list):
        if city in city_list:
            print(city + " exists!")


check_if_cities_exist()

# spreading existing tuple elements
city_list_appended = (*city_list, 'lahore')

print(city_list_appended)
print(type(city_list_appended))

# tuple -> list [then] list -> tuple
print(tuple(list(city_list_appended)))


def insert_at(n, item):
    # slicing on iterable returns an slice of that iterable. So both city_list_appended[:n] & city_list_appended[n:]
    # returns tuple. that's why following returns ... (tuple, item, tuple) ...

    # return (city_list_appended[:n], item, city_list_appended[n:])

    # tuple elements are being unpacked
    return *city_list_appended[:n], item, *city_list_appended[n:]


# slicing works on iterables not only on list
print(type(city_list_appended[:]))  # <class 'tuple'>
print(insert_at(3, 'new york'))


def get_first_and_last_city(cities):
    sorted_city_list = sorted(cities)
    return sorted_city_list[0], 'random city', sorted_city_list[-1], 'random city at the end'


first_city, _, second_city, _ = get_first_and_last_city(city_list_appended)
print(first_city, second_city)

name = "pycharm"

print(id(name))

name = "qrt"
print(id(name))

print(":".join(city_list_appended))
print(":".join(city_list_appended).partition(":"))  # partition returns a tuple of 3 elements


def get_partitions(yy):
    parts = yy.partition(':')
    elements = []
    empty = ''

    while parts[1] is not empty:
        elements.append(parts[0])
        parts = parts[2].partition(':')

    return elements


print(get_partitions(':'.join(city_list_appended)))

print('Age of {0} is {1}'.format('Jim', 88))
print('Age of {} is {}'.format('Jim', 88))
print("{1} is {0}'s age".format('Jim', 89))

# passing a whole module with 'm' as alias
print("math constants. pi={m.pi}, e={m.e}".format(m=math))
print(type(math))  # <class 'module'>

print("current coordinates: {latitude}, {longitude}".format(latitude=80.23, longitude=100))
print('first city from city list is [{}] & second city from city list is [{}]'.format(city_list_appended[0],
                                                                                      city_list_appended[-1]))

print(f'pi: {math.pi}')
