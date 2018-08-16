class Solution(object):
    
    def missing_number_by_indexing(self, nums):

        if nums:

            dic = [-1] * (len(nums) + 1)

            for x in nums:
                dic[x] = x

            missing_elements_arr = [i for i, y in enumerate(dic) if y == -1]

            if missing_elements_arr:
                return missing_elements_arr[0]

    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if nums:

            array_sum = sum(nums)
            expected_sum = (len(nums) * (len(nums) + 1)) / 2

            return int(expected_sum - array_sum)


s = Solution()
'''
print(s.missingNumber([3,0,1]))
print(s.missingNumber([9,6,4,2,3,5,7,0,1]))
'''

print(s.missing_number_by_indexing([3,0,1]))
print(s.missing_number_by_indexing([9,6,4,2,3,5,7,0,1]))
