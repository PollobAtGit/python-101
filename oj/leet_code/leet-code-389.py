class Solution(object):
    
    def find_diff_non_sorted(self, s, t):

        """
        worst case: if the extra character is one of the duplicate values
        complexity:
            O(n) + O(m) + O(distinct characters in t): n => len(s), m => len(t)
            O(m)
        """

        if s is not None and t is not None and abs(len(s) - len(t)) == 1:

            dic = {}

            for i, x in enumerate(s):
                if x not in dic:
                    dic[x] =[i]
                else:
                    dic[x].append(i)

            other_dic = {}

            for j, y in enumerate(t):
                if y not in dic:
                    return y
                elif y not in other_dic:
                    other_dic[y] = [j]
                else:
                    other_dic[y].append(j)

            for item in other_dic.items():
                if len(dic[item[0]]) != len(item[1]):
                    return t[(set(item[1]) - set(dic[item[0]])).pop()]


    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        """
        complexity:
            logn + logn + n : n => len(s) 
                O(n)
        """

        if s is not None and t is not None and abs(len(t) - len(s)) == 1:

            s = "".join(sorted(s))
            t = "".join(sorted(t))

            for i, x in enumerate(s):
                if x != t[i]:
                    return t[i]

            return t[-1]
        

s = Solution()

"""
assumption:
    there will be duplicate characters
    alpha-numeric characters

"""

"""
print(s.findTheDifference("abcd", "abcde"))
print(s.findTheDifference("", ""))
print(s.findTheDifference(None, ""))
print(s.findTheDifference(None, None))
print(s.findTheDifference("", "e"))
print(s.findTheDifference("", "e"))
print(s.findTheDifference("abcd", "acbde"))
print(s.findTheDifference("abcd", "tacbd"))

print(s.findTheDifference("ae", "aea"))

"""

print("other")

print(s.find_diff_non_sorted("abcd", "abcde"))
print(s.find_diff_non_sorted("", ""))
print(s.find_diff_non_sorted(None, ""))
print(s.find_diff_non_sorted(None, None))
print(s.find_diff_non_sorted("", "e"))
print(s.find_diff_non_sorted("", "e"))
print(s.find_diff_non_sorted("abcd", "acbde"))
print(s.find_diff_non_sorted("abcd", "tacbd"))

print(s.find_diff_non_sorted("ae", "aea"))

