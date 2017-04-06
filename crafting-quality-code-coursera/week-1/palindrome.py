
def is_palindrome_v1(s):
   return reverse(s) == s

    """
    (str) -> bool
    >>> is_palindrome_v1('noon')
    True
    >>> is_palindrome_v1('racecar')
    True
    >>> is_palindrome_v1(dented)
    False
    
    """

 


# POI: No return type mentioned here
# POI: No data type mentioning is required

def reverse(s):

    # POI: No data type is mentioned
    rev = ''

    for ch in s:
        # This works because the current character is the last character
        # at every step & essentially is becoming the first character
        rev = ch + rev

    # No return type is mentioned still we are returning value (same as JS)
    return rev
    
