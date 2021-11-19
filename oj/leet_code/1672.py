class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """

        if accounts:
            richestManAmount = 0

            for i in range(len(accounts)):

                runningWealthSum = 0

                for j in range(len(accounts[i])):
                    runningWealthSum = runningWealthSum + accounts[i][j]

                richestManAmount = max(richestManAmount, runningWealthSum)
            
            return richestManAmount
        

s = Solution()

assert s.maximumWealth([[1]]) == 1
assert s.maximumWealth([[1,2,3],[3,2,1]]) == 6
assert s.maximumWealth([[1,5],[7,3],[3,5]]) == 10
assert s.maximumWealth([[2,8,7],[7,1,3],[1,9,5]]) == 17

