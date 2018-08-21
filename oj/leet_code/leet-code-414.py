class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if nums:
            highest = nums[0]
            highest_2 = None
            highest_3 = None

            for x in nums[1:]:
                if x in [highest, highest_2, highest_3]:
                    continue
                if x > highest:
                    highest_3 = highest_2
                    highest_2 = highest
                    highest = x
                elif not highest_2 or x > highest_2:
                    highest_3 = highest_2
                    highest_2 = x
                elif not highest_3 or x > highest_3:
                    highest_3 = x

            return highest_3 if highest_3 is not None else highest

s = Solution()

print(s.thirdMax([3, 2, 1]))
print(s.thirdMax([1, 2]))

print(s.thirdMax([2, 2, 3, 1]))
print(s.thirdMax([1, 2, 3]))
print(s.thirdMax([2, -1, 3, 0]))
print(s.thirdMax([2, -1, 3, 0, 10, 20, 1]))
