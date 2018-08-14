# O(n) time and O(1) extra space

class Solution:
    def find_duplicates_in_an_array(self, A):

        if A:

            sorted_a = sorted(A)

            for i, x in enumerate(sorted_a):
                if (i + 1) < len(sorted_a) and x == sorted_a[i + 1]:
                    return x

            return -1

    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):

        """
        time complexity: O(len(A))
        space complexity: O(distinct characters in A)
        """

        if A:

            dic = {}

            for x in A:
                if x in dic:
                    dic[x] = dic[x] + 1
                else:
                    dic[x] = 1

            multiple = [y[0] for y in dic.items() if y[1] > 1]

            if multiple:
                return multiple[0]
            else:
                return -1

s = Solution()

print(s.repeatedNumber([3, 4, 1, 4, 1]))
print(s.repeatedNumber([4, 4]))

print(s.find_duplicates_in_an_array([3, 4, 1, 4, 1]))
print(s.find_duplicates_in_an_array([4, 4]))

