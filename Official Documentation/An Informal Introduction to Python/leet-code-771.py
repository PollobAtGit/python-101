from functools import reduce

class Solution(object):
    def numJewelsInStones(self, J, S):

        if J is not None and S is not None:
            J = list(J)
            S = list(S)
            
            J.sort()
            S.sort()

            return sum([S.count(i) for i in J])
            # return reduce(lambda x, y: (x + y), [S.count(i) for i in J], 0)      
        

    def numJewelsInStones_two(self, J, S):
        return len([i for i in J for j in S if i == j])

    def numJewelsInStones_set(self, J, S):

        js = {x: 0 for x in J}

        for x in S:
            if x in js.keys():
                js[x] += 1

        return sum(js.values())

s = Solution()

print(s.numJewelsInStones("aA", "aAAbbbb"))
print(s.numJewelsInStones("z", "ZZ"))
print(s.numJewelsInStones("", ""))
print(s.numJewelsInStones("", None))
print(s.numJewelsInStones(None, None))

print(sum([1, 2]))

print(s.numJewelsInStones_set("aA", "aAAbbbb"))
