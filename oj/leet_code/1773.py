class Solution:
    mapping = {
            "type": 0,
            "color": 1,
            "name": 2,
    }

    def countMatchesWithFor(self, items, ruleKey, ruleValue):
        if items and ruleKey and ruleValue:

            indexToSearch = self.mapping[ruleKey]
            ans = 0

            for line in items:
                if line[indexToSearch] == ruleValue:
                    ans = ans + 1

            return ans

    def countMatches(self, items, ruleKey, ruleValue):
        if items and ruleKey and ruleValue:

            indexToSearch = self.mapping[ruleKey]
            ans = 0
            i = 0
            while i < len(items):
                if items[i][indexToSearch] == ruleValue:
                    ans = ans + 1
                i = i + 1

            return ans

s = Solution()

assert s.countMatches([["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], "color", "silver")
assert s.countMatches([["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]], "type", "phone")
        
assert s.countMatchesWithFor([["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], "color", "silver")
assert s.countMatchesWithFor([["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]], "type", "phone")
