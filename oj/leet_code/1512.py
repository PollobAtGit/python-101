class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if nums:

            dic = {}

            i = 0

            while i < len(nums):

                v = nums[i]

                if v in dic:
                    dic[v].append(i)
                else:
                    dic[v] = [i]

                i = i + 1

            ans = []

            for _, key in enumerate(dic):

                k = 0

                v = dic[key]

                while k < len(v):

                    r = k + 1
                    
                    while r < len(v):
                        if v[k] < v[r]:
                            ans.append((v[k], v[r]));
                        r = r + 1

                    k = k + 1

            return len(ans)
        
s = Solution()

assert s.numIdenticalPairs([1]) == 0
assert s.numIdenticalPairs([1,2,3,1,1,3]) == 4
assert s.numIdenticalPairs([1,1,1,1]) == 6
assert s.numIdenticalPairs([1,2,3]) == 0

