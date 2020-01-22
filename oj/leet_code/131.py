class Solution(object):
    def decompressRLElist(self, nums):
        if nums is not None:
            l = []
            for i in range(len(nums) / 2):
                a, b = nums[2*i], nums[2*i + 1]
                l = l + ([b] * a)
            return l
