class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        v = 0

        for i in range(len(operations)):
            op = operations[i]

            if op == "--X" or op == "X--":
                v = v - 1
            if op == "++X" or op == "X++":
                v = v + 1

        return v
        
s = Solution()

assert s.finalValueAfterOperations(["--X"]) == -1
assert s.finalValueAfterOperations(["X--"]) == -1
assert s.finalValueAfterOperations(["++X"]) == 1
assert s.finalValueAfterOperations(["X++"]) == 1
assert s.finalValueAfterOperations(["++X","++X","X++"]) == 3
assert s.finalValueAfterOperations(["++X","++X","X++"]) == 3
