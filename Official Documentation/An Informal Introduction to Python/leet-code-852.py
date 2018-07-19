class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        # dic = {A[i]: i for i in range(len(A))}
        # return dic[max(dic)]

        return A.index(max(A))
        

s = Solution()
print(s.peakIndexInMountainArray([0,1,0]))
print(s.peakIndexInMountainArray([0,2,1,0]))
