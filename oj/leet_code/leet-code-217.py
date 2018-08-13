class Solution:
<<<<<<< HEAD
=======
    
    def contains_duplicate_by_sort(self, nums):

        if nums is not None:

            nums.sort()

            for i, _ in enumerate(nums):
                if (i + 1) < len(nums) and nums[i] == nums[i + 1]:
                    return True

            return False


>>>>>>> b2e6b6dea069ff886e9667018f8fe0426612188e
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

<<<<<<< HEAD
        if nums:

        	dic = {}

        	for x in nums:
        		if x is not None:
        			if dic.get(x):
        				return True
        			else:
        				dic[x] = None
=======
        if nums is not None:

            dic = {}

            for x in nums:
                if x is not None:
                    if dic.get(x):
                        return True
                    else:
                        dic[x] = 1

            return False
>>>>>>> b2e6b6dea069ff886e9667018f8fe0426612188e
        

s = Solution()

<<<<<<< HEAD
print(s.containsDuplicate([1,2,3,1]))
print(s.containsDuplicate([1,2,3,4]))
print(s.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
=======
"""
print(s.containsDuplicate([1,2,3,1]))
print(s.containsDuplicate([1,2,3,4]))
print(s.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
print(s.containsDuplicate(None))
print(s.containsDuplicate([]))
print(s.containsDuplicate([None]))
"""

print(s.contains_duplicate_by_sort([1,2,3,1]))
print(s.contains_duplicate_by_sort([1,2,3,4]))
print(s.contains_duplicate_by_sort([1,1,1,3,3,4,3,2,4,2]))
print(s.contains_duplicate_by_sort(None))
print(s.contains_duplicate_by_sort([]))
print(s.contains_duplicate_by_sort([None]))
>>>>>>> b2e6b6dea069ff886e9667018f8fe0426612188e
