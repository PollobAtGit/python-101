
if __name__ == "__main__":
    n  = int(input())
    columns = input().split()

    import collections

    Student = collections.namedtuple('Student', ",".join(columns))
    total_mark = 0
    for _ in range(n):
        attrs = input().split()
        total_mark += int(Student(*attrs).MARKS)

    print(total_mark / n)

