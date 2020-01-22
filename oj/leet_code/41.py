class Solution(object):

    def binary_search(self, nums, v):
        if nums is not None and v is not None:
            if len(nums) == 0:
                return False
            mid = int(len(nums) / 2)
            if nums[mid] == v:
                return True
            elif v > nums[mid]:
                return self.binary_search(nums[mid + 1:], v)
            return self.binary_search(nums[:mid], v)

    def firstMissingPositive(self, nums):
        if nums is not None:
            
            sorted_nums = sorted(nums)
            last_element = 0 if len(sorted_nums) == 0 else sorted_nums[len(sorted_nums) - 1]
            
            for i in range(1, last_element + 1):
                if not self.binary_search(sorted_nums[:], i):
                    return i
            return last_element + 1

    def firstMissingPositive(self, nums):
        if nums is not None:
           
            if len(nums) == 0:
                return 1
            
            sorted_nums = sorted(nums)
            positive_integer_index = None

            for i, x in enumerate(sorted_nums):
                if x >= 1:
                    positive_integer_index = i
                    break

            if positive_integer_index is None:
                return 1

            q = 1
            for i in range(positive_integer_index, len(sorted_nums)):
                if i + 1 < len(sorted_nums) and sorted_nums[i] == sorted_nums[i + 1]:
                    continue
                if sorted_nums[i] != q:
                    return q
                q += 1

            return q 

