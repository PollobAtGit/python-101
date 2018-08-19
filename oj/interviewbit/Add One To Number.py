class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):

        if A is not None:

            i = len(A) - 1
            ret = []

            carry = 1

            while i > -1:

                total_sum = A[i] + carry

                if total_sum > 9:
                    carry = 1
                    ret.append(0)
                else:
                    carry = 0
                    ret.append(total_sum)

                i = i - 1

            if carry == 1:
                ret.append(1)

            ret = ret[::-1]

            if ret[0] == 0:

                i = 1
                while i < len(ret):
                    if ret[i] != 0:
                        break
                    i = i + 1

                ret = ret[i:]

            return ret


s = Solution()

'''
print(s.plusOne([1, 2, 3]))
print(s.plusOne([9]))
print(s.plusOne([9, 9]))
print(s.plusOne([6, 9]))
print(s.plusOne([2, 3, 9, 9]))
'''
print(s.plusOne([ 0, 3, 7, 6, 4, 0, 5, 5, 5 ]))



