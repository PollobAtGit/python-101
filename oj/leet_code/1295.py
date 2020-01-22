class Solution(object):

    # 123 -> 3
    # 12 -> 2
    # 1 -> 1
    # 0

    def int_to_str(self, n):
        if n is not None:
            digits = []
            while n:
                digits.append(str(n % 10))
                n /= 10
            return "".join(digits[::-1])

    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums:
            res = 0
            for x in nums:
                if len(self.int_to_str(x)) % 2 == 0:
                # if len("{:d}".format(x).lstrip("0")) % 2 == 0:
                    res += 1
            return res
