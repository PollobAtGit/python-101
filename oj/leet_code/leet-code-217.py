class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if nums:

        	dic = {}

        	for x in nums:
        		if x is not None:
        			if dic.get(x):
        				return True
        			else:
        				dic[x] = None
        

s = Solution()

print(s.containsDuplicate([1,2,3,1]))
print(s.containsDuplicate([1,2,3,4]))
print(s.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))