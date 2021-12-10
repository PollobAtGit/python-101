from collections import deque


class Solution(object):
    def countStudents(self, students, sandwiches):
        if students and sandwiches:

            students = deque(students)
            sandwiches = deque(sandwiches)

            while sandwiches and students and len([x for x in students if x == sandwiches[0]]) > 0:

                currentStudent = students.popleft()

                if currentStudent == sandwiches[0]:
                    sandwiches.popleft()
                else:
                    students.append(currentStudent)

            return len(students)


s = Solution()

assert s.countStudents([1, 1, 0, 0], [0, 1, 0, 1]) == 0
assert s.countStudents([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1]) == 3
