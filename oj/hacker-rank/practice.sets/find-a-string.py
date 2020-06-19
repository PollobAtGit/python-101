if __name__ == "__main__":
    org_string = input()
    sub_string = input()

    total_cnt = 0
    indx = org_string.find(sub_string)

    while indx > -1:
        total_cnt = total_cnt + 1
        org_string = org_string[indx + 1:]
        indx = org_string.find(sub_string)

    print(total_cnt)
