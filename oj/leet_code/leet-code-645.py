class Solution:
    
    # not working try this one
    def find_error(self, nums):
        if nums is not None:
            i = 0
            while i < len(nums):

                while nums[i] != i + 1 and nums[nums[i] - 1] != nums[i] - 1:
                    nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i]
                i = i + 1

            print(nums)
            return [[x, i] for i, x in enumerate(nums) if i != x][0]

    def findErrorNums(self, nums):
        if nums is not None:
            cl_nums = [-1] * (len(nums) + 1)

            dup = None
            for x in nums:
                if dup is None and cl_nums[x] == x:
                    dup = cl_nums[x]
                cl_nums[x] = x

            return [dup, [i for i, x in enumerate(cl_nums) if x == -1 and i != 0][0]]

s = Solution()
print(s.findErrorNums([1,2,2,4]))
print(s.find_error([4,2,2,1]))
