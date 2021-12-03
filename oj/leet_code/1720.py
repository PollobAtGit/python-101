class Solution(object):
    def decode_improved(self, encoded, first):
        if encoded:
            ans = [first] + ([0] * len(encoded))

            i = 0

            while i < len(encoded):
                ans[i + 1] = ans[i] ^ encoded[i]
                i = i + 1

            return ans

    def decode(self, encoded, first):
        if encoded:

            ans = [first]

            i = 0

            while i < len(encoded):
                ans.append(encoded[i] ^ ans[len(ans) - 1:][0])
                i = i + 1

            return ans

s = Solution()

assert s.decode([1], 1) == [1,0]
assert s.decode([1,2,3], 1) == [1,0,2,1]
assert s.decode([6,2,7,3], 4) == [4,2,0,7,4]

assert s.decode_improved([1], 1) == [1,0]
assert s.decode_improved([1,2,3], 1) == [1,0,2,1]
assert s.decode_improved([6,2,7,3], 4) == [4,2,0,7,4]

