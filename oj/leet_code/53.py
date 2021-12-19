import sys


class Solution(object):
    def maxSubArray(self, nums):
        if nums:

            sumOfPreviousSubArray = -sys.maxsize-1
            totalMax = -sys.maxsize-1

            for i, v in enumerate(nums):
                sumOfPreviousSubArray = max(sumOfPreviousSubArray + v, v)
                totalMax = max(totalMax, sumOfPreviousSubArray)

            return totalMax


s = Solution()

assert s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
assert s.maxSubArray([1]) == 1
assert s.maxSubArray([5, 4, -1, 7, 8]) == 23
assert s.maxSubArray([-1]) == -1
