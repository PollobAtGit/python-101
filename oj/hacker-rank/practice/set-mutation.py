def init():
    return set([1, 3, 4]), set([3, 4, 66])

def play():

    print(init())

    s, q = init() 
    s.intersection_update(q) # keeps intersection of sets
    print(s)

    s, q = init() 
    s.update(q) # converts just to set
    print(s)

    s, q = init() 
    s.symmetric_difference_update(q) # converts just to set
    print(s)

    s, q = init() 
    s.difference_update(q) # converts just to set
    print(s)


if __name__ == "__main__":
    
    input()
   
    org_list = set(map(int, input().split()))
    
    op_cnt = int(input())

    while op_cnt:
        
        op = input().split()[0]

        nw_list = set(map(int, input().split()))

        if op == 'intersection_update':
            org_list.intersection_update(nw_list)
        elif op == 'update':
            org_list.update(nw_list)
        elif op == 'symmetric_difference_update':
            org_list.symmetric_difference_update(nw_list)
        else:
            org_list.difference_update(nw_list)

        op_cnt = op_cnt - 1 

    print(sum(org_list))

