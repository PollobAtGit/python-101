class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """

        sum_of_digits = num
        while sum_of_digits > 9:

            digits = []
            while sum_of_digits != 0:
                digits.append(sum_of_digits % 10)
                sum_of_digits = int(sum_of_digits / 10)

            sum_of_digits = sum(digits)

        return sum_of_digits

    def addDigits_one_liner(self, num):
        if num <= 9:
            return num
        return num % 9 if num % 9 != 0 else 9


s = Solution()
print(s.addDigits_one_liner(38))
