class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        if nums:

            for i in range(len(nums)):
                j = i - 1
                if j >= 0 and j < len(nums):
                    nums[i] = nums[j] + nums[i]

            return nums


s = Solution()

assert s.runningSum([0]) == [0]
assert s.runningSum([1]) == [1]
assert s.runningSum([1,2,3,4]) == [1,3,6,10]
assert s.runningSum([1,1,1,1,1]) == [1,2,3,4,5]
assert s.runningSum([3,1,2,10,1]) == [3,4,6,16,17]

