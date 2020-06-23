# Enter your code here. Read input from STDIN. Print output to STDOUT

# 9
# 1 2 3 4 5 6 7 8 9
# 10 11 21 55

# 1 2 3 4 5 6 7 8 9 10 11 21 55

input()
list_one = set(input().split())
input()
list_two = set(input().split())

unioned = list_one.union(list_two)

print(len(unioned))
