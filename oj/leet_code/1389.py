class Solution(object):
    # 20ms
    def createTargetArray_WithSlice(self, nums, index):
        if nums and index:
            ans = [-1] * len(nums)
            i = 0

            while i < len(nums):

                insert_at = index[i]
                insert_value = nums[i]

                if ans[insert_at] == -1:
                    ans[insert_at] = insert_value
                else:
                    ans = (ans [:insert_at] + [insert_value] + ans[insert_at:])[:len(nums)]

                i = i + 1

            return ans

    // 28ms
    def createTargetArray(self, nums, index):
        if nums and index:
            ans = [-1] * len(nums)
            i = 0

            while i < len(nums):

                insert_at = index[i]
                insert_value = nums[i]

                if ans[insert_at] == -1:
                    ans[insert_at] = insert_value
                else:

                    j = len(nums) - 1

                    while j >= 0 and insert_at < j:
                        ans[j] = ans[j - 1]
                        j = j - 1

                    ans[insert_at] = insert_value

                i = i + 1

            return ans


s = Solution()

assert s.createTargetArray([0,1,2,3,4], [0,1,2,2,1]) == [0,4,1,3,2]
assert s.createTargetArray([1,2,3,4,0], [0,1,2,3,0]) == [0,1,2,3,4]
assert s.createTargetArray([1], [0]) == [1]

assert s.createTargetArray_WithSlice([0,1,2,3,4], [0,1,2,2,1]) == [0,4,1,3,2]
assert s.createTargetArray_WithSlice([1,2,3,4,0], [0,1,2,3,0]) == [0,1,2,3,4]
assert s.createTargetArray_WithSlice([1], [0]) == [1]

