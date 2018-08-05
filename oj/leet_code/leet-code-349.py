class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        if nums1 is None: return []
        if nums2 is None: return []

        return list(set(nums1).intersection(nums2))
        

s = Solution()

print(s.intersection([1, 2, 2, 1], [2, 2]))
print(s.intersection(None, []))
