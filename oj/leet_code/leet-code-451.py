class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        if s:

            freq_counter = {}

            for x in s:
                if x in freq_counter:
                    freq_counter[x] = freq_counter[x] + 1
                else:
                    freq_counter[x] = 1

            return "".join([q[0] * q[1] for q in sorted(freq_counter.items(), key = lambda x: x[1], reverse = True)])
        return ""


s = Solution()
print(s.frequencySort("tree"))
print(s.frequencySort("cccaaa"))
print(s.frequencySort("Aabb"))
print(s.frequencySort(""))
print(s.frequencySort(None))
