class Solution(object):
    def getConcatenation(self, nums):
        if nums:

            i = 0
            l = len(nums)

            while i < l:
                nums.append(nums[i])
                i = i + 1

            return nums

        
s = Solution()

assert s.getConcatenation([1]) == [1, 1]
assert s.getConcatenation([1, 2]) == [1, 2, 1, 2]
assert s.getConcatenation([1,3,2,1]) == [1,3,2,1,1,3,2,1]

