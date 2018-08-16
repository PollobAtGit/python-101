class Solution:
    # @param A : integer
    # @return a list of strings
    def fizzBuzz(self, A):

        if A is not None:

            ret = []
            for x in range(1, A + 1):
                if x % 3 == 0 and x % 5 == 0:
                    ret.append('FizzBuzz')
                elif x % 3 == 0:
                    ret.append('Fizz')
                elif x % 5 == 0:
                    ret.append('Buzz')
                else:
                    ret.append(x)

            return ret


s = Solution()
print(s.fizzBuzz(5))
# print(s.fizzBuzz(20))
# print(s.fizzBuzz(31))
print(s.fizzBuzz(3))
