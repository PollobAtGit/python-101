class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        if candies:
            current_max = max(candies)

            i = 0
            while i < len(candies):
                candies[i] = current_max <= candies[i] + extraCandies
                i = i + 1

            return candies
        
s = Solution()

assert s.kidsWithCandies([2,3,5,1,3], 3) == [True,True,True,False,True] 
assert s.kidsWithCandies([4,2,1,1,2], 1) == [True,False,False,False,False] 
assert s.kidsWithCandies([12,1,12], 10) == [True,False,True]

