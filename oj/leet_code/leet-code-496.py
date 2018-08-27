"""
    Not accepted
"""


class Solution:

    def index_of(self, x, nums):
        if x is not None and nums is not None:
            for i, y in enumerate(nums):
                if y == x:
                    return i
            return None

    def nextGreaterElement(self, nums1, nums2):
        
        if nums1 is not None and nums2 is not None:

            ret = []

            for i, x in enumerate(nums1):
                first_index_of_x = self.index_of(x, nums2)
                if first_index_of_x is not None:
                    has_found = False
                    for y in nums2[first_index_of_x + 1:]:
                        if y > x:
                            ret.append(y)
                            has_found = True
                            break

                    if not has_found:
                        ret.append(-1)

            return ret



s = Solution()
print(s.nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))
print(s.nextGreaterElement([2, 4], [1, 2, 3, 4]))
print(s.nextGreaterElement([], [1, 2, 3, 4]))
print(s.nextGreaterElement([1], [1, 2, 3, 4]))
print(s.nextGreaterElement([1, -1], [1, 2, 3, 4]))
