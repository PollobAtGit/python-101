def check_strict_superset():
    
    a = set(input().split())
    
    itr_cnt = int(input())

    while itr_cnt:
        intermediary_set = set(input().split())
    
        if not (len(intermediary_set - a) == 0 and len(a - intermediary_set) > 0):
            return "False"
    
        itr_cnt = itr_cnt - 1
    
    return "True"

if __name__ == "__main__":
    print(check_strict_superset())
