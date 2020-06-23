# Given an integer, , perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of 2 to 5, print Not Weird
# If  is even and in the inclusive range of 6 to 20, print Weird
# If  is even and greater than 20 , print Not Weird

def if_else(n):
    if n is not None:
        if n % 2 == 1:
            return "Weird"
        if n >= 2 and n <= 5:
            return "Not Weird"
        if n >= 6 and n <= 20:
            return "Weird"
        return "Not Weird"
        
if __name__ == "__main__":
    n = int(input())
    print(if_else(n))

