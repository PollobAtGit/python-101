class Solution(object):
    
    
    def two_pointer_approach_2(self, nums, val):
        
        if nums is not None:

            i = 0

            while i < len(nums):
                
                if nums[i] == val:
                    del nums[i]
                else:
                    i = i + 1

            return len(nums)


    def two_pointer_approach(self, nums, val):
        
        # this solution is accepted because that requires the array to be inplace modified
        if nums is not None:

            i = 0

            for x in nums:
                if x != val:
                    i = i + 1

            return i


    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        if nums is not None:

            indices = [i for i, x in enumerate(nums) if x == val]

            i = 0

            for i_del in indices:
                del nums[i_del - i]
                i = i + 1            

            return len(nums)

        

s = Solution()
"""
print(s.two_pointer_approach([3,2,2,3], 3))
print(s.two_pointer_approach([0,1,2,2,3,0,4,2], 2))
print(s.two_pointer_approach([], 12))
print(s.two_pointer_approach(None, 12))
print(s.two_pointer_approach([1, 2, 3], 12))
"""

print(s.two_pointer_approach_2([3,2,2,3], 3))
print(s.two_pointer_approach_2([0,1,2,2,3,0,4,2], 2))
print(s.two_pointer_approach_2([], 12))
print(s.two_pointer_approach_2(None, 12))
print(s.two_pointer_approach_2([1, 2, 3], 12))

