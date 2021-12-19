class Solution(object):
    def containsDuplicateWithSort(self, nums):
        if nums:

            nums = sorted(nums)
            i = 0
            while i < len(nums):
                if i + 1 < len(nums) and nums[i] == nums[i+1]:
                    return True
                i = i + 1

            return False

    def containsDuplicate(self, nums):
        if nums:
            return len(set(nums)) != len(nums)


s = Solution()

assert s.containsDuplicate([1, 2, 3, 1]) == True
assert s.containsDuplicate([1, 2, 3, 4]) == False
assert s.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True
assert s.containsDuplicate([1]) == False

assert s.containsDuplicateWithSort([1, 2, 3, 1]) == True
assert s.containsDuplicateWithSort([1, 2, 3, 4]) == False
assert s.containsDuplicateWithSort([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True
assert s.containsDuplicateWithSort([1]) == False
