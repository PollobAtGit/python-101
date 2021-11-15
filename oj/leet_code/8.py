class Solution(object):

    def isNegativeOrPositive(self, v):
        q = ord(v)
        return q == 43 or q == 45

    def myAtoi(self, s):

        if not s.lstrip():
            return 0

        s = s.lstrip()

        if not (s[0].isdigit() or self.isNegativeOrPositive(s[0])):
            return 0

        isNegative = s[0] == "-"

        i = 0
        j = 1 if isNegative or s[0] == "+" else 0 

        while j < len(s):
            if s[j].isdigit():
                j = j + 1
            else:
                break

        num = s[1:j] if isNegative or s[0] == "+" else s[:j]

        if not num:
            return 0

        result = 0
        k = len(num) - 1
        q = 0
        
        # print("num", num, isNegative)

        while q < len(num):
            result = result + (int(num[q]) * pow(10, k))
            k = k - 1
            q = q + 1

        v = -1 * result if isNegative else result

        # print(v, v < -2147483648)

        if v < -2147483648:
            return -2147483648
        
        if v > 2147483647:
            return 2147483647
        
        return v

    def _myAtoi(self, s):
        
        s = s.lstrip()

        if not (s[0].isdigit() or self.isNegativeOrPositive(s[0])):
            return 0
        
        for i in range(1, len(s)):
            if not (s[i].isdigit() or self.isNegativeOrPositive(s[i])):
                break

        if i == len(s) - 1:
            i = i + 1

        print(s[:i])

        q = int("".join(s[:i]))
        
        if q < -2147483648:
            return -2147483648
        
        if q > 2147483647:
            return 2147483647
        
        return q
                
        
s = Solution()

assert s.myAtoi("42") == 42
assert s.myAtoi("   -42") == -42
assert s.myAtoi("4193 with words") == 4193
assert s.myAtoi("words and 987") == 0
assert s.myAtoi("+-12") == 0
assert s.myAtoi("-91283472332") == -2147483648
assert s.myAtoi("") == 0
assert s.myAtoi(" ")== 0


# assert s.myAtoi("words and 987") == 1


