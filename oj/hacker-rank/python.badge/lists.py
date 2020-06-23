if __name__ == "__main__":

    command_cnt = int(input())

    lst = []

    while command_cnt:
        
        parts = input().split()
        
        cmd = parts[0]

        if cmd == "insert":

            index = int(parts[1])
            element_to_insert = int(parts[2])

            lst = lst[:index] + [element_to_insert] + lst[index:]
        elif cmd == "print":
            print(lst)
        elif cmd == "remove":
            lst.remove(int(parts[1]))
        elif cmd == "append":
            lst = lst + [int(parts[1])]
        elif cmd == "sort":
            lst.sort()
        elif cmd == "pop":
            lst.pop()
        else:
            lst.reverse()

        command_cnt = command_cnt - 1
