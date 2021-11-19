class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """

        if nums and n:

            i = 0
            j = n
            length = len(nums)

            while i < length:
                k = i + 2
                q = None
                while k < length:
                    if k != j:
                        store = nums[k + 1]
                        nums[k + 1] = q
                        q = store
                    k = k + 1

                nums[i + 1] = nums[j]

                j = j + 1
                i = i + 2

            return nums
        
s = Solution()

assert s.shuffle([2,5], 1) == [2,5] 
assert s.shuffle([2,5,1,3,4,7], 3) == [2,3,5,4,1,7] 
assert s.shuffle([1,2,3,4,4,3,2,1], 4) == [1,4,2,3,3,2,4,1]
assert s.shuffle([1,1,2,2], 2) == [1,2,1,2]
