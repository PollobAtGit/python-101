"""
    Not accepted
"""


class Solution:


    def next_greater_element_dic(self, nums1, nums2):
        if nums1 is not None and nums2 is not None:

            dic = {}

            for x in nums2:

                if x not in dic :
                    dic[x] = None

                for y, t in dic.items():
                    if t is None:
                        if x > y:
                            dic[y] = x

            # print(dic)
            nge_for_all = {y: -1 if not t else t for y, t in dic.items()}
            # print(nge_for_all)
            return [nge_for_all[x] for x in nums1]


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
print(s.next_greater_element_dic([4, 1, 2], [1, 3, 4, 2]))
print(s.next_greater_element_dic([2, 4], [1, 2, 3, 4]))
print(s.next_greater_element_dic([], [1, 2, 3, 4]))
print(s.next_greater_element_dic([1], [1, 2, 3, 4]))
# print(s.next_greater_element_dic([1, -1], [1, 2, 3, 4]))
print(s.next_greater_element_dic([5, 6, 7, 4, 1, 10], [5, 6, 7, 4, 1, 10]))
