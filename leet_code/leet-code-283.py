class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        # if nums is None or len(nums) == 0: return []
        # if len(nums) == 1: return nums

        i = 0
        d = 0
        while i < len(nums):
            if nums[i] == 0:
                d =  d + 1
                del nums[i]
            else:
                i = i + 1

        for x in range(d):
            nums.append(0)
        
    
    def moveZeroes_c(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        if nums is None or len(nums) == 0: return []
        if len(nums) == 1: return nums

        indices = [x for  x in nums if x != 0]

        zs = len(nums) - len(indices)

        if zs > 0:
            indices = indices + [0 for x in range(zs)]

        nums[:] = indices

    def moveZeroes_ret(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        if nums is None or len(nums) == 0: return []
        if len(nums) == 1: return nums

        indices = [x for  x in nums if x != 0]

        zs = len(nums) - len(indices)

        if zs > 0:
            indices = indices + [0 for x in range(zs)]

        return indices


        

s = Solution()

"""
print(s.moveZeroes([0,1,0,3,12]))
print(s.moveZeroes([]))
print(s.moveZeroes([0]))
print(s.moveZeroes([0, 0]))
print(s.moveZeroes([0, 0, 0]))
print(s.moveZeroes([1, 0, 0]))
print(s.moveZeroes_ret([0, 1, 0]))
"""

v = [0, 0, 1]
s.moveZeroes(v)
print(v)

v = [0,1,0,3,12]
s.moveZeroes(v)
print(v)

v = [0,0,1]
s.moveZeroes(v)
print(v)

v = []
s.moveZeroes(v)
print(v)

v = [0, 0, 0]
s.moveZeroes(v)
print(v)
