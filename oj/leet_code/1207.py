class Solution(object):
    def uniqueOccurrences(self, arr):
        if arr is not None:
            import collections
            c = collections.Counter(arr)
                        
            q = [c for _, c in c.items()]
            
            return len(set(q)) == len(q)
