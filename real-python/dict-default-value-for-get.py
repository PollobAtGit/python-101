default_value = '1000'

cache = { 'HP': 56, 'APPLE': 700 }

def get_from_cache(key):
    # upon failure to get hit error will be thrown
    return cache[key]

def get_from_cache_by_get_api(key):
    return cache.get(key)

def get_or_default(key, use_get_api = False):
    if use_get_api:
        v = get_from_cache_by_get_api(key) 
        if v is None:
            return default_value
        return v
    else:
        try:
            return get_from_cache(key)
        except KeyError:
            return default_value

print(get_or_default('HP'))
print(get_or_default('P-HP'))

print(get_or_default('HP', True))
print(get_or_default('P-HP', True))

# remove lots of code for default value using dict.get(key, default_value) api

print(cache.get('HP', default_value))
print(cache.get('P-HP', default_value))
