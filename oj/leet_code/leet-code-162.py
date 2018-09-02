class Solution:
    def findPeakElement(self, nums):
        if nums is not None:
            for i, _ in enumerate(nums):
                if i - 1 >= 0 and i + 1 < len(nums):
                    if nums[i - 1] < nums[i] and nums[i] > nums[i + 1]:
                        return i
                elif i == 0:
                    if i + 1 < len(nums):
                        if nums[i] > nums[i + 1]:
                            return i
                    else:
                        return i
                elif i + 1 == len(nums):
                    if nums[i] > nums[i - 1]:
                        return i

s = Solution()
print(s.findPeakElement([1,2,3,1]))
print(s.findPeakElement([1,2,1,3,5,6,4]))
print(s.findPeakElement([1]))
print(s.findPeakElement([3,2,1]))
print(s.findPeakElement([10, 9, 8, 7]))



