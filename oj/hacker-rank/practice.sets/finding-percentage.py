if __name__ == "__main__":
    stdnt_cnt = int(input())

    stdnt_list = {}

    while stdnt_cnt:
        input_parts = input().split()
        
        stdnt_list[input_parts[0]] = sum([float(p) for p in input_parts[1:]]) / 3

        stdnt_cnt = stdnt_cnt - 1

    print('{0:.2f}'.format(stdnt_list[input()]))


