class Solution(object):
    def merge(self, nums1, m, nums2, n):
        if nums1 is not None and nums2 is not None and m is not None and n is not None:
            if n == 0:
                return
            if m == 0:
                i = 0
                while i < len(nums2):
                    nums1[i] = nums2[i]
                    i += 1
                return

            index = 0

            for i, v in enumerate(nums2):
                numDup = nums1[:m + i]
                while index < len(numDup):
                    q = numDup[index]
                    if v > q:
                        index += 1
                    else:
                        break

                shiftIndex = len(nums1) - 2
                while index <= shiftIndex:
                    nums1[shiftIndex + 1] = nums1[shiftIndex]
                    shiftIndex -= 1

                nums1[index] = v


s = Solution()


v = [1, 2, 3, 0, 0, 0]

s.merge(v, 3, [2, 5, 6], 3)
assert v == [1, 2, 2, 3, 5, 6]

v = [1]
s.merge(v, 1, [], 0)
assert v == [1]

v = [0]
s.merge(v, 0, [1], 1)
assert v == [1]
