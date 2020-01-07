class Solution(object):
    def _binary_search(self, arr, v, i, j):
        if arr is not None and v is not None:
            if not i < j:
                return -1
            mid = i + int((j - i) / 2)
            if arr[mid] == v:
                return mid
            elif v > arr[mid]:
                return self._binary_search(arr, v, mid + 1, j)
            return self._binary_search(arr, v, i, mid - 1)

    def search(self, nums, target):
        if nums is not None and target is not None:
           return self._binary_search(nums, target, 0, len(nums) - 1) 
