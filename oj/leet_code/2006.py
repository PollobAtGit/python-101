class Solution(object):
    def countKDifference(self, nums, k):
        if nums and k:
            
            ans = 0
            requiredList = {}

            for num in nums:
                if num in requiredList:
                    ans += requiredList[num]

                if num - k > 0:
                    requiredList[num - k] = 1 if requiredList.get(num - k) is None else requiredList[num - k] + 1

                requiredList[num + k] = 1 if requiredList.get(num + k) is None else requiredList[num + k] + 1

            return ans

s = Solution()

assert s.countKDifference([1,2,2,1], 1) == 4
assert s.countKDifference([1,3], 3) == 0
assert s.countKDifference([3,2,1,5,4], 2) == 3
    
