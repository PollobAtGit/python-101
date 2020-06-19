if __name__ == "__main__":
    org_string = input()

    r = False
    for ch in org_string:
        if ch.isalnum():
            r = True
            break

    print(r)

    r = False
    for ch in org_string:
        if ch.isalpha():
            r = True
            break

    print(r)
    
    r = False
    for ch in org_string:
        if ch.isdigit():
            r = True
            break

    print(r)

    r = False
    for ch in org_string:
        if ch.islower():
            r = True
            break

    print(r)
    
    r = False
    for ch in org_string:
        if ch.isupper():
            r = True
            break

    print(r)

