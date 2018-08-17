class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        if nums is not None:

            duplicates = []
            for x in nums:

                # we are negating values in array
                indx = abs(x) - 1
                if nums[indx] < 0:
                    # the value has been previously negated
                    duplicates.append(abs(x))
                else:
                    nums[indx] = nums[indx] * -1

            return duplicates
        return []


s = Solution()

print(s.findDuplicates([4,3,2,7,8,2,3,1]))
print(s.findDuplicates([]))
print(s.findDuplicates([1, 1]))

