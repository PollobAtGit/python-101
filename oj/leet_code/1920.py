class Solution(object):
    def buildArray(self, nums):

        if nums:

            arr = []
            i = 0

            while i < len(nums):
                arr.append(nums[nums[i]])
                i = i + 1

            return arr
       

s = Solution()

assert s.buildArray([0]) == [0]
assert s.buildArray([0,2,1,5,3,4]) == [0,1,2,4,5,3]
assert s.buildArray([5,0,1,2,3,4]) == [4,5,0,1,2,3]
