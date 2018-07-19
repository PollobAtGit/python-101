class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """

        for i_l in A:
            o_l_len = len(i_l)

            if o_l_len % 2 != 0:
                i_l[int(o_l_len / 2)] = 0 if i_l[int(o_l_len / 2)]== 1 else 1
                
            for i in range(int(o_l_len / 2)):
                j = o_l_len - (i + 1)

                # swap
                i_l[i], i_l[j] = i_l[j], i_l[i]

                # flip
                i_l[i] = 0 if i_l[i]== 1 else 1
                i_l[j] = 0 if i_l[j]== 1 else 1

        return A

s = Solution()
print(s.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))
print(s.flipAndInvertImage([[1,1,0]]))
print(s.flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))  
