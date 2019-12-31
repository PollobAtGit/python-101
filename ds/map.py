
dns_resolver = {
    'http://www.google.com': '45.56.89.78',
    'http://www.yahoo.com': '45.56.89.79',
}


def print_all(dic):
    for k, v in dic.items():
        print(k, ' = ', v)
    print()


def find_in_map(hash_map, item_to_find):
    if item_to_find in hash_map:
        return item_to_find + " = " + hash_map[item_to_find]
    return "not found"


def modify_in_map(hash_map, key, value):
    if key in hash_map:
        hash_map[key] = value
    return None


print_all(dns_resolver)
print(find_in_map(dns_resolver, "ty"))
print(find_in_map(dns_resolver, "http://www.google.com"))
print()

modify_in_map(dns_resolver, "http://www.google.com", "89")
modify_in_map(dns_resolver, "http://www.le.com", "89")

print_all(dns_resolver)

del dns_resolver['http://www.yahoo.com']
print_all(dns_resolver)
