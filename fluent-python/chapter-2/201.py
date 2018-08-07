symbols = '$¢r£¥€¤ca'

symbol_asciis = [ord(ch) for ch in symbols]

print(symbol_asciis)  # [36, 162, 163, 165, 8364, 164]

unicode_characters = [{ch: ord(ch)}for ch in symbols if ord(ch) > 127]
non_unicode_characters = [{ch: ord(ch)} for ch in symbols if ord(ch) < 127]

print(unicode_characters)
print(non_unicode_characters)
