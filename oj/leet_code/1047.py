'''
Input: "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
'''

class Solution(object):
    def removeDuplicates_new(self, s):
        if s is not None:
            stck = []
            i = 0
            while i < len(s):
                if len(stck) > 0:
                    top = stck[len(stck) - 1]
                    if s[i] == top:
                        stck = stck[:len(stck) - 1]
                    else:
                        stck.append(s[i])
                else:
                    stck.append(s[i])
                i = i + 1
            return "".join(stck)


    def removeDuplicates(self, s):
        if s is not None:
            stck = []
            i = 0
            while i < len(s):
                if len(stck) > 0:
                    top = stck[len(stck) - 1]
                    if s[i] == top:
                        while i < len(s) and s[i] == top:
                            i = i + 1
                        stck = stck[:len(stck) - 1]
                    else:
                        stck.append(s[i])
                        i = i + 1
                else:
                    stck.append(s[i])
                    i = i + 1
            
            if len(stck) == 0:
                stck = s[0]

            return "".join(stck)


s = Solution()
print(s.removeDuplicates_new("aaaaaaaa"))
print(s.removeDuplicates_new("aaaaaaaaa"))

