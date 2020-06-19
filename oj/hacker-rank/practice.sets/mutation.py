if __name__ == "__main__":
    string = input()
    parts = input().split()
    string_as_list = list(string)
    index = int(parts[0])

    print("".join(string_as_list[:index] + [parts[1]] + string_as_list[index+1:]))


