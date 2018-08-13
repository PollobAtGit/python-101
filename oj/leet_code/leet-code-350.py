def intersect(nums1, nums2):
    # print(s.intersect_by_set(nums1, nums2))
    # print(s.intersect(nums1, nums2))
    print(s.intersection_when_sorted_array(nums1, nums2))

class Solution(object):

    def intersection_when_sorted_array(self, A, B):

        """
            complexity: O(t) where t = max(len(m), len(n))
        """
        
        nums1 = A
        nums2 = B
        
        if nums1 and nums2:
            
            i = 0
            j = 0

            intersect = []

            while i < len(nums1) and j < len(nums2):

                if nums1[i] == nums2[j]:
                    
                    intersect.append(nums1[i])

                    i = i + 1
                    j = j + 1

                elif nums1[i] > nums2[j]:
                    j = j + 1

                # elif nums1[i] < nums2[j]:
                else:
                    i = i + 1

            return intersect


        return []

    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        """
            complexity: O(n) + O(m) + O(max(distinct count in n, distinct count in m))
        """

        if nums1 and nums2:

            def make_hash_table(arr):
                
                dic = {}

                for x in arr:
                    if x in dic:
                        dic[x] = dic[x] + 1
                    else:
                        dic[x] = 1

                return dic

            def get_intersection(dic_one, dic_two):
                intr = []
                for x in dic_one.items():
                    if x[0] in dic_two:
                        intr = intr + [x[0] for t in range(0, min(x[1], dic_two[x[0]]))]

                return intr

            num_one_dic = make_hash_table(nums1)
            num_two_dic = make_hash_table(nums2)

            # print(num_one_dic)
            # print(num_two_dic)

            intersection = get_intersection(num_one_dic, num_two_dic) \
                                if len(num_one_dic) > len(num_two_dic) \
                                else get_intersection(num_two_dic, num_one_dic)

            return intersection

        return []

    def intersect_by_set(self, nums1, nums2):
        if nums1 and nums2:
            return list(set(nums1) & set(nums2))
        

s = Solution()

"""
intersect([1,2,2,1], [2,2])# 2 2
intersect([4,9,5], [9,4,9,8,4])# 4 9
intersect([4,9,4], [9,4,9,8,4])# 4 4 9
"""

intersect([1,1,2,2], [2,2])# 2 2
intersect([4,5, 9], [4, 4, 8, 9,9])# 4 9
intersect([4,4, 9], [4,4,8,9,9,])# 4 4 9
