def sort_by_first_element_then_by_():
    q = [[1, 'd'], [0, 'b'], [1, 'c']]
    print(q)
    print(sorted(q, key=lambda x: (x[0], x[1])))

if __name__ == "__main__":
    # sort_by_first_element_then_by_()

    stdnt_cnt = int(input())

    stdnt_list = []
    
    while stdnt_cnt:
        stdnt_list.append([input(), float(input())])
        stdnt_cnt = stdnt_cnt - 1

    # print(sorted(stdnt_list, key=lambda x: (-x[1], x[0])))
    
    sorted_by_grade = sorted(stdnt_list, key=lambda x: (x[1], x[0]))
    
    # print(sorted_by_grade[1][0], sorted_by_grade[2][0], end=' ')

    second_lowest_grade = sorted(set([x[1] for x in sorted_by_grade]))[1]

    # print(*[x[0] for x in sorted_by_grade if x[1] == second_lowest_grade], end='\n')
    
    second_lowest_grade_scorers = [x[0] for x in sorted_by_grade if x[1] == second_lowest_grade]

    for x in second_lowest_grade_scorers:
        print(x)

