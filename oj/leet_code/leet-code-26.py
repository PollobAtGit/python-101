class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if nums is not None:

            i = 0 

            while i < len(nums):

                if (i + 1) < len(nums) and nums[i] == nums[i + 1]:
                    del nums[i + 1]
                else:
                    i = i + 1

            return len(nums)

    def by_inplace_replcement(self, nums):

        if nums is not None:

            if len(nums) < 2:
                return len(nums)

            i = 0
            j = 1

            while i < len(nums) and j < len(nums):

                if (i + 1) < len(nums) and nums[i] != nums[j]:
                    i = i +1
                    nums[i] = nums[j]

                j = j +1                   


            return i + 1
                


        

s = Solution()

"""

print(s.removeDuplicates([1,1,2]))
print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
print(s.removeDuplicates([]))
print(s.removeDuplicates(None))

"""

print(s.by_inplace_replcement([1,1,1, 2]))
print(s.by_inplace_replcement([0,0,1,1,1,2,2,3,3,4]))
print(s.by_inplace_replcement([]))
print(s.by_inplace_replcement(None))
