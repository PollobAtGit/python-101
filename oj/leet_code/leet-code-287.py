class Solution:
    def findDuplicate(self, nums):
        if nums is not None:

            for x in nums:
                if abs(x) < len(nums):
                    c = nums[abs(x)]
                    if c < 0:
                        return abs(x)
                    else:
                        nums[abs(x)] = -1 * nums[abs(x)]

s = Solution()
print(s.findDuplicate([1,3,4,2,2]))
print(s.findDuplicate([3,1,3,4,2]))
print(s.findDuplicate([2,2,2,2,2]))