from pymemcache.client import base
import time

client = base.Client(('localhost', 11211))

def get_browser_name():
    # return "google-chrome"
    # return "opera"
    return "internet explorer"

def set_cache_value(key, value):
    if client:
        try:
            client.set(key, value)
        except Exception as e:
            return None
        finally:
            print('saved [%s] as %s' % (value, key))

def get_cache_value(key):
    if key:
        value = None
        try:
            value = client.get(key)
        except Exception as e:
            return None
        finally:
            if value:
                print('retrieved value of [%s]' % key)
            else:
                print('didnt find value for %s' % key)

        return value

browser_key = 'other-browser-ie-2'

browser_data = get_cache_value(browser_key)

if browser_data is None:
    set_cache_value(browser_key, get_browser_name())
    browser_data = get_cache_value(browser_key)


print(browser_data)
