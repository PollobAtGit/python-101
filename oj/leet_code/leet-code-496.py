"""
    Not accepted
"""


class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        def internal(indx):
            if indx + 1 < len(nums2):
                for y in nums2[indx:]:
                    if y > nums1[indx]:
                        return y
                return -1

        ret_array = []
        for i, _ in enumerate(nums1):
            ret_array.append(internal(i))

        return ret_array


s = Solution()
print(s.nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))
print(s.nextGreaterElement([2, 4], [1, 2, 3, 4]))
