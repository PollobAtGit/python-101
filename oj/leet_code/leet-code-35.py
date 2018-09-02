class Solution:
    def binary(self, nums, start, end, target):
        if nums is not None and target is not None:
            if start < end:

                mid = int(start + ((end - start) / 2))

                if nums[mid] == target:
                    return mid

                if nums[mid] > target:
                    return self.binary(nums, start, mid - 1, target)
                else:
                    return self.binary(nums, mid + 1, end, target)
            else:
                if nums[start] == target:
                    return start
                if nums[start] > target:
                    return start
                return start + 1

    def searchInsert(self, nums, target):
        if nums is not None and target is not None:
            return self.binary(nums, 0, len(nums) - 1, target)


'''
            # if len(nums) == 1:
            if 
                if nums[0] == target:
                    return True
                else:
                    return False



                print(mid)
                print(nums[mid] > target)
                print(nums[mid])
                input()
'''

s = Solution()

'''
print(s.searchInsert([1,3,5,6], 5))
print(s.searchInsert([1,3,5,6], 2))
'''

print(s.binary([1,3,5,6], 0, len([1,3,5,6]) - 1, -1))
