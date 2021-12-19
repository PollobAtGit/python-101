class Solution(object):
    def restoreString(self, s, indices):
        if s and indices:
            s = list(s)
            hasBeenProcessed = set()

            prevReplacedValue = s[indices[0]]
            prevReplacedIndex = 0
            
            while len(hasBeenProcessed) < len(s):
                
                index = indices[prevReplacedIndex]

                store = s[index]
                s[index] = prevReplacedValue

                prevReplacedValue = store
                prevReplacedIndex = index

                hasBeenProcessed.add(index)

                print(hasBeenProcessed)

            print(s)
            return "".join(s)
        
s = Solution()

# assert s.restoreString("abc", [0,1,2]) == "abc"
assert s.restoreString("aiohn", [3,1,4,2,0]) == "nihao"
assert s.restoreString("aaiougrt", [4,0,2,6,7,3,1,5]) == "arigatou"
assert s.restoreString("art", [1,0,2]) == "rat"

