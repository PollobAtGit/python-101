# 1st argument is general argument
# 2nd argument is a tuple (because of the *)
# 3rd argument is a dictionary/map (because of the **)

def cheeseshop(kind, *arguments, **keywords):
    print("--Do you have any ", kind, "?")
    print("We are out of stock for ", kind)

    for arg in arguments:
        print(arg)

    print("*" * 50)

    for key in keywords:
        print(key ," -> ", keywords[key])

# Sinle star method argument can take indfinite number of arguments
def write_multiple_items(*js_type_arguments):
    for arg in js_type_arguments:
        print(str(arg))

def i_concat_strings(*strings_to_concat, seperator="|"):
    # seprator joins strings
    joined_string = seperator.join(strings_to_concat)
    print(joined_string)

def ranging_from_list_by_argument(i_donot_know_who_i_am):
    # star before argument SPREADS the sequence/array
    # to seperate elements of the list
    print(list(range(*i_donot_know_who_i_am)))

def parrot(voltage, state="a stiff", action="voom"):
    print(voltage, " -> ", state, " -> ", action)

def what_is_lambda(n):
    return lambda x: x + n

cheeseshop("Ferrari", "We are very sorry sir", "we are very very sorry"
           , shopkeeper = "Plain", client = "Cheese",
           sketch = "other sketch")

write_multiple_items("1", "2", "3", "4", 5)

i_concat_strings("1", "2", "others")

# Passing tuple or array/sequence?
ranging_from_list_by_argument([8, 15])

# note the spread operator (**) for dictionary before the dictionary
parrot(**{
    "voltage": "123",
    "state": 894,
    "action": 3**8
    })

i_am_lambda = what_is_lambda(10)

print(i_am_lambda(18))
print(i_am_lambda(25))
