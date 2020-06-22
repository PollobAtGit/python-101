import math

if __name__ == "__main__":
    org_str = list(input())
    width = int(input())

    wrapped_str = [] 

    cnt = math.ceil(len(org_str) / width)

    for i in range(cnt):
        wrapped_str +=  (['\n'] if len(wrapped_str) != 0 else []) + org_str[:width]
        org_str = org_str[width:]

    print("".join(wrapped_str))

