class Solution:

    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        if nums is not None:

            if len(nums) < 2:
                return []

            nums_set = {x for x in nums}
            all_nums = {x for x in range(1, len(nums) + 1)}

            rest_of_the_nums = all_nums - nums_set

            return [x for x in rest_of_the_nums]


s = Solution()
print(s.findDisappearedNumbers_not_using_set([4, 3, 2, 7, 8, 2, 3, 1]))
print(s.findDisappearedNumbers_not_using_set([]))
print(s.findDisappearedNumbers_not_using_set(None))
print(s.findDisappearedNumbers_not_using_set([1]))
print(s.findDisappearedNumbers_not_using_set([1, 1]))
