class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        if nums:

            ans = []

            i = 0 

            while i < len(nums):

                j = 0

                ans.append(0)

                while j < len(nums):
                    
                    if i != j and nums[j] < nums[i]:
                        ans[i] = ans[i] + 1

                    j = j + 1

                i = i + 1

            return ans

        
s = Solution()

assert s.smallerNumbersThanCurrent([1, 2]) == [0, 1]
assert s.smallerNumbersThanCurrent([2, 1]) == [1, 0]
assert s.smallerNumbersThanCurrent([2, 2]) == [0, 0]
assert s.smallerNumbersThanCurrent([8,1,2,2,3]) == [4,0,1,1,3]
assert s.smallerNumbersThanCurrent([6,5,4,8]) == [2,1,0,3]
assert s.smallerNumbersThanCurrent([7,7,7,7]) == [0,0,0,0]

