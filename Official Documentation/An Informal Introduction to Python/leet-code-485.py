class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if nums is None or len(nums) == 0: return 0

        max_count = 0
        c_run = 0

        for x in nums:
            if x == 1:
                c_run = c_run + 1
            elif x == 0:
                max_count = max(max_count, c_run)
                c_run = 0

        return max(max_count, c_run)
        
        

s = Solution()
print(s.findMaxConsecutiveOnes([1,1,0,1,1,1]))
print(s.findMaxConsecutiveOnes([1,1,1,1,1,1]))
print(s.findMaxConsecutiveOnes([0,0,0,0,0,0]))
print(s.findMaxConsecutiveOnes([0,0,0,1,0,0]))
print(s.findMaxConsecutiveOnes([0,1,0,1,0,0]))
print(s.findMaxConsecutiveOnes([0,1,1,1,0,0]))
print(s.findMaxConsecutiveOnes([]))
print(s.findMaxConsecutiveOnes(None))
