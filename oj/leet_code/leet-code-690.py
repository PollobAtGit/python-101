# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees, id):
        if id is not None and employees is not None:
            dic = {}

            for x in employees:
                dic[x.id] = (x.importance, x.subordinates)

            if id in dic:
                employee = dic[id]

                total_importance = employee[0]
                subordinates = employee[1]

                while subordinates:

                    next_subs_to_check = []
                    for y in subordinates:
                        if y in dic:
                            total_importance = total_importance + dic[y][0]
                            next_subs_to_check = next_subs_to_check + dic[y][1]

                    subordinates = next_subs_to_check

                return total_importance

s = Solution()
# print(s.getImportance([[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1))
print(s.getImportance([Employee(1, 5, [2, 3]), Employee(2, 3, []), Employee(3, 3, [])], 1))

# [[1,5,[2,3]],[2,3,[4]],[3,4,[]],[4,1,[]]], 1
print(s.getImportance([Employee(1, 5, [2, 3]), Employee(2, 3, [4]), Employee(3, 4, []), Employee(4, 1, [])], 1))
