class Solution(object):
    def targetIndices(self, nums, target):
        if nums:
            
            v = sorted(nums)

            i = 0
            ans = []

            while i < len(v) and v[i] <= target:
                if v[i] == target:
                    ans.append(i)
                i = i + 1

            return ans
       
s = Solution()

assert s.targetIndices([1], 2) == []
assert s.targetIndices([1], 1) == [0]
assert s.targetIndices([1,2,5,2,3], 2) == [1, 2]
assert s.targetIndices([1,2,5,2,3], 3) == [3]
assert s.targetIndices([1,2,5,2,3], 4) == []

