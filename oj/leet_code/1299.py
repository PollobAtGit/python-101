class Solution(object):
    def replace_elements(self, arr):
        if arr is not None:
            if len(arr) == 0:
                return []
            if len(arr) == 1:
                return [-1]
            if len(arr) == 2:
                return [arr[1], -1]
            
            r = [arr[len(arr) - 1], -1]
            l = max(arr[len(arr) - 2:])
            for i in range(len(arr) - 3, -1, -1):
                r = [l] + r
                if arr[i] > l:
                    l = arr[i]
            return r

    def replaceElements(self, arr):
        if arr is not None:
            r = []
            for i, x in enumerate(arr):
                r.append(sorted(arr[i + 1:])[::-1][0] if i + 1 < len(arr) else -1)
            return r
